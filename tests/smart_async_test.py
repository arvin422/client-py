"""SMART exchanges verify pinned endpoints and signed patient evidence."""

import base64
import hashlib
import json
import unittest
from urllib.parse import parse_qs, urlsplit

import httpx
import jwt
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key

from fhirclient.smart import (
    ClientSecretBasic,
    ExchangeUncertain,
    InvalidIdentity,
    Login,
    TokenRejected,
    Verification,
    authorization_url,
    exchange,
    refresh,
    revoke,
    verify,
)


class SmartAsyncTest(unittest.IsolatedAsyncioTestCase):
    async def test_verified_launch_and_explicit_refresh_and_revocation(self):
        key = generate_private_key(public_exponent=65537, key_size=2048)
        public = json.loads(
            jwt.algorithms.RSAAlgorithm.to_jwk(key.public_key())
        )
        public["kid"] = "signing"
        config = Login(
            verification=Verification(
                actor_kind="patient",
                client_id="client +:",
                issuer="https://ehr.test/fhir",
                fhir_base="https://ehr.test/fhir",
                jwks_endpoint="https://ehr.test/keys",
            ),
            authorize_endpoint="https://ehr.test/authorize",
            token_endpoint="https://ehr.test/token",
            callback="https://app.test/callback",
            authentication=ClientSecretBasic("secret +:"),
        )
        now = 1700000000
        verifier = "v" * 64
        nonce = "retained-nonce"
        scopes = "openid fhirUser patient/Patient.r offline_access"
        url = authorization_url(
            config,
            state="retained-state",
            nonce=nonce,
            verifier=verifier,
            scopes=tuple(scopes.split()),
            launch="ehr-launch",
        )
        query = parse_qs(urlsplit(url).query)
        self.assertEqual(query["aud"], [config.verification.fhir_base])
        self.assertEqual(
            query["code_challenge"],
            [
                base64.urlsafe_b64encode(
                    hashlib.sha256(verifier.encode()).digest()
                )
                .decode()
                .rstrip("=")
            ],
        )
        claims = {
            "iss": config.verification.issuer,
            "aud": config.verification.client_id,
            "sub": "subject",
            "iat": now,
            "exp": now + 300,
            "nonce": nonce,
            "fhirUser": "Patient/patient",
            "at_hash": base64.urlsafe_b64encode(
                hashlib.sha256(b"access").digest()[:16]
            )
            .decode()
            .rstrip("="),
        }
        calls = []
        wrong_endpoint, reject_refresh, lost = False, False, False

        def respond(request):
            calls.append(request)
            path = request.url.path
            if path.endswith("smart-configuration"):
                return httpx.Response(
                    200,
                    json={
                        "authorization_endpoint": config.authorize_endpoint,
                        "token_endpoint": "https://other.test/token"
                        if wrong_endpoint
                        else config.token_endpoint,
                    },
                )
            if path == "/keys":
                return httpx.Response(200, json={"keys": [public]})
            if path == "/fhir/Patient/patient":
                self.assertEqual(
                    request.headers["authorization"], "Bearer access"
                )
                return httpx.Response(
                    200,
                    json={
                        "resourceType": "Patient",
                        "id": "patient",
                        "name": [{"text": "Test Patient"}],
                    },
                )
            self.assertEqual(
                base64.b64decode(
                    request.headers["authorization"].removeprefix("Basic ")
                ).decode(),
                "client+%2B%3A:secret+%2B%3A",
            )
            form = parse_qs(request.content.decode())
            if path == "/revoke":
                self.assertEqual(form["token"], ["rotated"])
                return httpx.Response(200)
            if lost:
                raise httpx.ReadTimeout("lost exchange", request=request)
            if form["grant_type"] == ["refresh_token"]:
                if reject_refresh:
                    return httpx.Response(400, json={"error": "invalid_grant"})
                return httpx.Response(
                    200,
                    json={
                        "access_token": "new-access",
                        "refresh_token": "rotated",
                        "token_type": "bearer",
                        "expires_in": 300,
                        "scope": scopes,
                    },
                )
            self.assertEqual(form["code_verifier"], [verifier])
            return httpx.Response(
                200,
                json={
                    "id_token": jwt.encode(
                        claims,
                        key,
                        algorithm="RS256",
                        headers={"kid": "signing"},
                    ),
                    "access_token": "access",
                    "refresh_token": "offline",
                    "token_type": "bearer",
                    "expires_in": 300,
                    "scope": scopes,
                    "patient": "patient",
                },
            )

        async with httpx.AsyncClient(
            transport=httpx.MockTransport(respond)
        ) as http:
            result = await exchange(
                config,
                http.send,
                code="one-use",
                verifier=verifier,
                nonce=nonce,
                now=now,
            )
            self.assertEqual(result.identity.patient_id, "patient")
            self.assertEqual(result.identity.actor_name, "Test Patient")
            self.assertEqual(result.tokens.refresh_token, "offline")
            self.assertEqual(len(calls), 4)
            refreshed = await refresh(
                config, http.send, refresh_token="offline", now=now
            )
            self.assertEqual(refreshed.refresh_token, "rotated")
            await revoke(
                config,
                http.send,
                endpoint="https://ehr.test/revoke",
                token="rotated",
                now=now,
            )
            reject_refresh = True
            with self.assertRaises(TokenRejected) as error:
                await refresh(
                    config, http.send, refresh_token="rejected", now=now
                )
            self.assertEqual(error.exception.code, "invalid_grant")
            self.assertEqual(len(calls), 7)
            lost = True
            with self.assertRaises(ExchangeUncertain):
                await refresh(
                    config, http.send, refresh_token="unknown", now=now
                )
            self.assertEqual(len(calls), 8)
            # A changed discovery endpoint prevents credentials leaving the pin.
            wrong_endpoint = True
            with self.assertRaises(InvalidIdentity):
                await exchange(
                    config,
                    http.send,
                    code="unused",
                    verifier=verifier,
                    nonce=nonce,
                    now=now,
                )
            self.assertEqual(len(calls), 9)
            # Signed identity must also bind the independently supplied token.
            result.tokens.access_token = "substituted"
            with self.assertRaises(InvalidIdentity):
                await verify(
                    config.verification,
                    result.tokens,
                    http.send,
                    nonce=nonce,
                    now=now,
                )
            self.assertEqual(
                [item.url.path for item in calls[-2:]],
                ["/fhir/.well-known/smart-configuration", "/keys"],
            )
            self.assertFalse(http.is_closed)
