"""Typed async FHIR operations over an owned or borrowed HTTP connection."""

import re
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from enum import Enum
from typing import Annotated, TypeVar
from urllib.parse import urljoin, urlsplit

import httpx
import msgspec

from .models.bundle import Bundle
from .models.fhirabstractbase import FHIRValidationError, JSONValue
from .models.operationoutcome import OperationOutcome, OperationOutcomeIssue
from .models.resource import Resource
from .models.valueset import ValueSet

T = TypeVar("T", bound=Resource)
Send = Callable[[httpx.Request], Awaitable[httpx.Response]]
Observe = Callable[[httpx.Response], Awaitable[None]]
ResourceId = Annotated[str, msgspec.Meta(pattern=r"^[A-Za-z0-9.-]{1,64}$")]
_ID: msgspec.json.Decoder[ResourceId] = msgspec.json.Decoder(ResourceId)


class Limits(msgspec.Struct, forbid_unknown_fields=True):
    pages: Annotated[int, msgspec.Meta(gt=0)] = 16
    records: Annotated[int, msgspec.Meta(gt=0)] = 64
    bytes: Annotated[int, msgspec.Meta(gt=0)] = 65536


class SearchFailure(str, Enum):
    TRANSPORT = "transport"
    REJECTED = "rejected"
    MALFORMED = "malformed"
    PAGINATION = "pagination"
    LIMIT = "limit"
    INCOMPLETE = "incomplete"


class ResourceFailureReason(str, Enum):
    INVALID_JSON = "invalid_json"
    RESOURCE_TYPE = "resource_type"
    FIELD_VALIDATION = "field_validation"
    MISSING_ID = "missing_id"
    ID_MISMATCH = "id_mismatch"


class ResourceFailure(msgspec.Struct, kw_only=True):
    reason: ResourceFailureReason
    path: Annotated[str, msgspec.Meta(pattern=r"^[A-Za-z0-9_.]{0,256}$")] = ""


class ResourceDecodeError(ValueError):
    """Generated resource validation failed, with no patient values exposed."""

    def __init__(self, failure: ResourceFailure) -> None:
        self.failure = failure
        super().__init__(failure.reason.value)


class RequestError(Exception):
    """A received response did not satisfy the requested FHIR interaction."""

    def __init__(
        self,
        reason: SearchFailure,
        status: int | None = None,
        issues: tuple[OperationOutcomeIssue, ...] = (),
        failure: ResourceFailure | None = None,
    ) -> None:
        self.reason = reason
        self.status = status
        self.issues = issues
        self.failure = failure
        super().__init__(reason.value)


class Created(msgspec.Struct, tag="created"):
    resource_id: ResourceId


class Rejected(msgspec.Struct, tag="rejected"):
    status: int


class Uncertain(msgspec.Struct, tag="uncertain"):
    pass


def _model(kind: type[T], value: JSONValue) -> T:
    if not isinstance(value, dict) or (
        value.get("resourceType") != kind.resource_type
    ):
        raise ResourceDecodeError(
            ResourceFailure(reason=ResourceFailureReason.RESOURCE_TYPE)
        )
    try:
        return kind(value)
    except FHIRValidationError as error:
        raise ResourceDecodeError(
            ResourceFailure(
                reason=ResourceFailureReason.FIELD_VALIDATION,
                path=_validation_path(error),
            )
        ) from None


def _validation_path(error: FHIRValidationError) -> str:
    path = error.path or ""
    child = next(
        (
            item
            for item in error.errors
            if isinstance(item, FHIRValidationError)
        ),
        None,
    )
    if child is not None:
        path = ".".join(filter(None, (path, _validation_path(child))))
    return path if re.fullmatch(r"[A-Za-z0-9_.]{0,256}", path) else ""


def decode(kind: type[T], payload: bytes) -> T:
    """Validate a resource using its generated R4 definition."""
    try:
        return msgspec.json.Decoder(kind, dec_hook=_model).decode(payload)
    except msgspec.ValidationError as error:
        if isinstance(error.__cause__, ResourceDecodeError):
            raise error.__cause__ from None
        raise ResourceDecodeError(
            ResourceFailure(reason=ResourceFailureReason.FIELD_VALIDATION)
        ) from None
    except msgspec.DecodeError:
        raise ResourceDecodeError(
            ResourceFailure(reason=ResourceFailureReason.INVALID_JSON)
        ) from None


def encode(value: Resource) -> bytes:
    """Serialize a resource, including generated-model validation."""
    try:
        return msgspec.json.encode(value.as_json())
    except FHIRValidationError as error:
        raise ValueError("Invalid FHIR resource") from error


def _issues(response: httpx.Response) -> tuple[OperationOutcomeIssue, ...]:
    try:
        return tuple(decode(OperationOutcome, response.content).issue or [])
    except (ValueError, TypeError, msgspec.DecodeError):
        return ()


@dataclass(slots=True)
class AsyncFHIRClient:
    """Borrow a send capability; operations never acquire or close its pool."""

    base: str
    send: Send
    limits: Limits = field(default_factory=Limits)

    def __post_init__(self) -> None:
        self.base = self.base.rstrip("/")
        target = urlsplit(self.base)
        if (
            target.scheme not in ("http", "https")
            or not target.hostname
            or target.username is not None
            or target.query
            or target.fragment
            or "%" in target.path
            or any(part in (".", "..") for part in target.path.split("/"))
        ):
            raise ValueError("Expected a FHIR base URL")
        self.limits = msgspec.json.decode(
            msgspec.json.encode(self.limits), type=Limits
        )

    async def _get(
        self,
        request: httpx.Request,
        observe: Observe | None,
    ) -> httpx.Response:
        try:
            response = await self.send(request)
        except (OSError, httpx.HTTPError):
            raise RequestError(SearchFailure.TRANSPORT) from None
        if observe is not None:
            await observe(response)
        if len(response.content) > self.limits.bytes:
            raise RequestError(SearchFailure.LIMIT, response.status_code)
        if response.status_code != 200:
            raise RequestError(
                SearchFailure.REJECTED, response.status_code, _issues(response)
            )
        return response

    def _request(
        self, path: str, parameters: tuple[tuple[str, str], ...] = ()
    ) -> httpx.Request:
        return httpx.Request(
            "GET",
            self.base + "/" + path,
            params=parameters,
            headers={
                "accept": "application/fhir+json",
                "cache-control": "no-cache",
            },
        )

    async def read(
        self,
        kind: type[T],
        identifier: str,
        *,
        observe: Observe | None = None,
    ) -> T:
        identifier = msgspec.convert(identifier, type=ResourceId)
        if identifier in (".", ".."):
            raise ValueError("FHIR identity is not a safe URL segment")
        response = await self._get(
            self._request(kind.resource_type + "/" + identifier), observe
        )
        try:
            value = decode(kind, response.content)
            if value.id != identifier:
                raise ResourceDecodeError(
                    ResourceFailure(
                        reason=(
                            ResourceFailureReason.MISSING_ID
                            if value.id is None
                            else ResourceFailureReason.ID_MISMATCH
                        ),
                        path="id",
                    )
                )
            return value
        except ResourceDecodeError as error:
            raise RequestError(
                SearchFailure.MALFORMED,
                response.status_code,
                failure=error.failure,
            ) from None
        except (ValueError, TypeError, msgspec.DecodeError):
            raise RequestError(
                SearchFailure.MALFORMED, response.status_code
            ) from None

    async def search(
        self,
        kind: type[T],
        parameters: tuple[tuple[str, str], ...] = (),
        *,
        observe: Observe | None = None,
    ) -> list[T]:
        records: dict[str, T] = {}
        visited: set[str] = set()
        total: int | None = None
        received = 0
        request = self._request(kind.resource_type, parameters)
        while len(visited) < self.limits.pages:
            location = str(request.url)
            if location in visited:
                raise RequestError(SearchFailure.PAGINATION)
            visited.add(location)
            response = await self._get(request, observe)
            received += len(response.content)
            if received > self.limits.bytes:
                raise RequestError(SearchFailure.LIMIT)
            try:
                bundle = decode(Bundle, response.content)
                if bundle.type != "searchset":
                    raise ValueError("Expected a FHIR search set")
                if len(bundle.entry or []) > self.limits.records:
                    raise RequestError(SearchFailure.LIMIT)
                if bundle.total is not None:
                    if bundle.total < 0 or (
                        total is not None and total != bundle.total
                    ):
                        raise RequestError(SearchFailure.INCOMPLETE)
                    total = bundle.total
                for entry in bundle.entry or []:
                    value = entry.resource
                    if isinstance(value, OperationOutcome):
                        raise RequestError(
                            SearchFailure.INCOMPLETE,
                            issues=tuple(value.issue or []),
                        )
                    if not isinstance(value, kind) or value.id is None:
                        raise ValueError("Unexpected resource in search set")
                    identifier = msgspec.convert(value.id, type=ResourceId)
                    previous = records.get(identifier)
                    if previous is not None and (
                        previous.as_json() != value.as_json()
                    ):
                        raise RequestError(SearchFailure.INCOMPLETE)
                    records[identifier] = value
                if len(records) > self.limits.records:
                    raise RequestError(SearchFailure.LIMIT)
                links = [
                    link.url
                    for link in bundle.link or []
                    if link.relation == "next"
                ]
                if not links:
                    if total is not None and total != len(records):
                        raise RequestError(SearchFailure.INCOMPLETE)
                    return list(records.values())
                if len(links) != 1 or links[0] is None:
                    raise RequestError(SearchFailure.PAGINATION)
                following = urljoin(location, links[0])
                target, pinned = urlsplit(following), urlsplit(self.base)
                if (
                    (target.scheme, target.netloc)
                    != (pinned.scheme, pinned.netloc)
                    or not target.path.startswith(pinned.path + "/")
                    or target.username is not None
                    or target.fragment
                    or "%" in target.path
                    or any(
                        part in (".", "..") for part in target.path.split("/")
                    )
                ):
                    raise RequestError(SearchFailure.PAGINATION)
                request = httpx.Request(
                    "GET", following, headers=request.headers
                )
            except (ValueError, TypeError, msgspec.DecodeError):
                raise RequestError(
                    SearchFailure.MALFORMED, response.status_code
                ) from None
        raise RequestError(SearchFailure.LIMIT)

    async def expand(
        self,
        parameters: tuple[tuple[str, str], ...],
        *,
        observe: Observe | None = None,
    ) -> ValueSet:
        response = await self._get(
            self._request("ValueSet/$expand", parameters), observe
        )
        try:
            return decode(ValueSet, response.content)
        except (ValueError, TypeError, msgspec.DecodeError):
            raise RequestError(
                SearchFailure.MALFORMED, response.status_code
            ) from None

    async def create(self, value: Resource) -> Created | Rejected | Uncertain:
        payload = encode(value)
        if len(payload) > self.limits.bytes:
            raise ValueError("FHIR resource exceeds its byte limit")
        endpoint = self.base + "/" + value.resource_type
        try:
            response = await self.send(
                httpx.Request(
                    "POST",
                    endpoint,
                    content=payload,
                    headers={
                        "accept": "application/fhir+json",
                        "content-type": "application/fhir+json",
                    },
                )
            )
        except (OSError, httpx.HTTPError):
            return Uncertain()
        if response.status_code in (400, 401, 403, 404, 422):
            return Rejected(response.status_code)
        if response.status_code != 201:
            return Uncertain()
        if response.content and len(response.content) <= self.limits.bytes:
            try:
                fields = msgspec.json.decode(
                    response.content, type=dict[str, msgspec.Raw]
                )
                if (
                    msgspec.json.decode(fields["resourceType"], type=str)
                    == value.resource_type
                ):
                    return Created(_ID.decode(fields["id"]))
            except (KeyError, ValueError, msgspec.DecodeError):
                pass
        location = response.headers.get("location", "")
        resolved = urljoin(endpoint + "/", location)
        suffix = resolved.removeprefix(endpoint + "/")
        if (
            location
            and resolved.startswith(endpoint + "/")
            and not urlsplit(resolved).query
            and not urlsplit(resolved).fragment
            and re.fullmatch(
                r"[A-Za-z0-9.-]{1,64}(?:/_history/[A-Za-z0-9.-]{1,64})?",
                suffix,
            )
        ):
            return Created(suffix.split("/")[0])
        return Uncertain()


@asynccontextmanager
async def async_client(
    base: str,
    *,
    limits: Limits | None = None,
    timeout: float = 10,
    transport: httpx.AsyncBaseTransport | None = None,
) -> AsyncGenerator[AsyncFHIRClient, None]:
    """Own a standalone pool and close every response, including cancellation."""
    selected = Limits() if limits is None else limits
    async with httpx.AsyncClient(
        timeout=timeout,
        trust_env=False,
        follow_redirects=False,
        transport=transport,
    ) as http:

        async def send(request: httpx.Request) -> httpx.Response:
            response = await http.send(request, stream=True)
            try:
                body = bytearray()
                async for chunk in response.aiter_bytes(chunk_size=4096):
                    if len(chunk) > selected.bytes - len(body):
                        raise OSError("HTTP response exceeds size limit")
                    body.extend(chunk)
                headers = response.headers.copy()
                _ = headers.pop("content-encoding", None)
                _ = headers.pop("content-length", None)
                return httpx.Response(
                    response.status_code, headers=headers, content=bytes(body)
                )
            finally:
                await response.aclose()

        yield AsyncFHIRClient(base, send, selected)
