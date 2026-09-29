"""Async operations retain completeness, write uncertainty, and ownership."""

import asyncio
import unittest

import httpx

from fhirclient.async_client import (
    AsyncFHIRClient,
    Created,
    Limits,
    RequestError,
    SearchFailure,
    Uncertain,
    async_client,
)
from fhirclient.models.observation import Observation
from fhirclient.models.patient import Patient


class AsyncClientTest(unittest.IsolatedAsyncioTestCase):
    async def test_borrowed_search_archives_before_validation(self):
        bodies = [
            b'{"resourceType":"Bundle","type":"searchset","total":2,'
            b'"entry":[{"resource":{"resourceType":"Patient","id":"one"}}],'
            b'"link":[{"relation":"next","url":"?page=2"}]}',
            b'{"resourceType":"Bundle","type":"searchset","total":2,'
            b'"entry":[{"resource":{"resourceType":"Patient","id":"two"}}]}',
        ]
        calls, observed = [], []

        def respond(request):
            calls.append(str(request.url))
            return httpx.Response(200, content=bodies[len(calls) - 1])

        async def archive(response):
            observed.append(response.content)

        async with httpx.AsyncClient(
            transport=httpx.MockTransport(respond)
        ) as http:
            client = AsyncFHIRClient("https://ehr.test/fhir", http.send)
            records = await client.search(Patient, observe=archive)
            self.assertEqual([item.id for item in records], ["one", "two"])
            self.assertEqual(observed, bodies)
            self.assertFalse(http.is_closed)
            self.assertEqual(calls[-1], "https://ehr.test/fhir/Patient?page=2")
            calls.clear()
            observed.clear()
            bodies[:] = [
                b'{"resourceType":"Bundle","type":"searchset",'
                b'"link":[{"relation":"next","url":"https://other.test/Patient"}]}'
            ]
            with self.assertRaises(RequestError) as error:
                await client.search(Patient, observe=archive)
            self.assertEqual(error.exception.reason, SearchFailure.PAGINATION)
            self.assertEqual(observed, bodies)
            self.assertEqual(len(calls), 1)
            calls.clear()
            bodies[:] = [b'{"resourceType":"Patient","active":"invalid"}']
            with self.assertRaises(RequestError) as error:
                await client.search(Patient, observe=archive)
            self.assertEqual(error.exception.reason, SearchFailure.MALFORMED)
            self.assertEqual(observed[-1], bodies[0])

    async def test_create_is_validated_and_sent_once(self):
        calls = []
        lost = True

        def respond(request):
            calls.append(request)
            if lost:
                raise httpx.ReadTimeout("response lost", request=request)
            return httpx.Response(
                201,
                headers={
                    "location": "https://ehr.test/fhir/Observation/created/_history/1"
                },
            )

        async with httpx.AsyncClient(
            transport=httpx.MockTransport(respond)
        ) as http:
            client = AsyncFHIRClient("https://ehr.test/fhir", http.send)
            with self.assertRaises(ValueError):
                await client.create(Observation())
            self.assertEqual(calls, [])
            observation = Observation(
                {
                    "resourceType": "Observation",
                    "status": "final",
                    "code": {"text": "Measurement"},
                    "valueInteger": 12,
                }
            )
            self.assertIsInstance(await client.create(observation), Uncertain)
            self.assertEqual(len(calls), 1)
            lost = False
            self.assertEqual(
                await client.create(observation), Created("created")
            )
            self.assertEqual(len(calls), 2)
            self.assertEqual(calls[0].content, calls[1].content)

    async def test_owned_transport_closes_on_limits_and_cancellation(self):
        entered = asyncio.Event()
        release = asyncio.Event()

        class Body(httpx.AsyncByteStream):
            closed = False
            bounded = False

            async def __aiter__(self):
                entered.set()
                if not self.bounded:
                    await release.wait()
                yield b"x" * 8192

            async def aclose(self):
                self.closed = True

        class Transport(httpx.AsyncBaseTransport):
            closed = False
            body = Body()

            async def handle_async_request(self, request):
                return httpx.Response(200, stream=self.body, request=request)

            async def aclose(self):
                self.closed = True

        transport = Transport()
        async with async_client(
            "https://ehr.test/fhir",
            transport=transport,
            limits=Limits(bytes=4096),
        ) as client:
            task = asyncio.create_task(client.read(Patient, "one"))
            await entered.wait()
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            self.assertTrue(transport.body.closed)
            transport.body = Body()
            transport.body.bounded = True
            with self.assertRaises(RequestError):
                await client.read(Patient, "one")
            self.assertTrue(transport.body.closed)
        self.assertTrue(transport.closed)
        with self.assertRaises(RuntimeError):
            await client.read(Patient, "one")
