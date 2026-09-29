"""Passive SMART protocol values, independent of application persistence."""

from collections.abc import Callable
from enum import Enum
from typing import Annotated, Literal
from urllib.parse import urlsplit

import msgspec
from msgspec import Meta, Struct

from .async_client import ResourceId


class Check(str, Enum):
    DISCOVERY_RESPONSE = "discovery_response"
    DISCOVERY_ENDPOINTS = "discovery_endpoints"
    TOKEN_EXCHANGE = "token_exchange"
    TOKEN_RESPONSE = "token_response"
    SCOPE_OPENID = "scope_openid"
    SCOPE_FHIR_USER = "scope_fhir_user"
    SCOPE_PATIENT_READ = "scope_patient_read"
    SCOPE_PRACTITIONER_READ = "scope_practitioner_read"
    JWKS_RESPONSE = "jwks_response"
    JWT_HEADER = "jwt_header"
    JWT_KEY = "jwt_key"
    JWT_CLAIMS = "jwt_claims"
    JWT_LIFETIME = "jwt_lifetime"
    JWT_NONCE = "jwt_nonce"
    ACCESS_TOKEN_HASH = "access_token_hash"
    FHIR_USER = "fhir_user"
    FHIR_ACTOR_RESPONSE = "fhir_actor_response"
    FHIR_PATIENT_RESPONSE = "fhir_patient_response"
    FHIR_IDENTITY = "fhir_identity"


class SmartTokens(
    Struct, kw_only=True, forbid_unknown_fields=False, omit_defaults=True
):
    id_token: Annotated[str, Meta(max_length=16384, min_length=1)]
    access_token: Annotated[str, Meta(max_length=16384, min_length=1)]
    patient: ResourceId
    scope: Annotated[str, Meta(min_length=1, max_length=4096)]
    token_type: Annotated[str, Meta(pattern="^(?i:bearer)$")]

    refresh_token: (
        Annotated[str, Meta(min_length=1, max_length=16384)] | None
    ) = None
    expires_in: Annotated[int, msgspec.Meta(gt=0)] | None = None

    def __repr__(self) -> str:
        return "SmartTokens(<redacted>)"


class SmartDiscovery(Struct, forbid_unknown_fields=False):
    authorization_endpoint: Annotated[str, Meta(max_length=1024, min_length=1)]
    token_endpoint: Annotated[str, Meta(max_length=1024, min_length=1)]


class OidcClaims(
    Struct, kw_only=True, forbid_unknown_fields=False, omit_defaults=True
):
    iss: Annotated[str, Meta(max_length=1024, min_length=1)]
    aud: Annotated[str, Meta(max_length=256, min_length=1)]
    sub: Annotated[str, Meta(max_length=1024, min_length=1)]
    nonce: Annotated[str, Meta(min_length=1, max_length=1024)] | None = None
    at_hash: Annotated[str, Meta(pattern="^[A-Za-z0-9_-]{22}$")] | None = None
    exp: Annotated[int, msgspec.Meta(gt=0)]
    iat: Annotated[int, msgspec.Meta(ge=0)]
    nbf: Annotated[int, msgspec.Meta(ge=0)] | None = None


class SmartClaims(OidcClaims, kw_only=True, rename="camel"):
    fhir_user: Annotated[str, Meta(max_length=2048, min_length=1)]


class OidcHeader(
    Struct, kw_only=True, forbid_unknown_fields=False, omit_defaults=True
):
    alg: Literal["RS256"]
    kid: Annotated[str, Meta(max_length=256, min_length=1)] | None = None
    crit: Annotated[list[str], Meta(max_length=0)] | None = None
    b64: bool | None = None


class OidcKey(
    Struct, kw_only=True, forbid_unknown_fields=False, omit_defaults=True
):
    kty: Annotated[str, Meta(max_length=16, min_length=1)]
    n: Annotated[str, Meta(max_length=2048, min_length=1)] | None = None
    e: Annotated[str, Meta(max_length=16, min_length=1)] | None = None
    kid: Annotated[str, Meta(max_length=256, min_length=1)] | None = None
    use: Annotated[str, Meta(max_length=16, min_length=1)] | None = None
    key_ops: list[str] | None = None
    alg: Annotated[str, Meta(max_length=32, min_length=1)] | None = None


class OidcKeys(
    Struct, kw_only=True, forbid_unknown_fields=False, omit_defaults=True
):
    keys: Annotated[list[OidcKey], Meta(max_length=16, min_length=1)]


class CheckResult(str, Enum):
    COMPLETED = "completed"
    AWAITING = "awaiting"
    REJECTED = "rejected"
    UNCONFIRMED = "unconfirmed"


class CheckEvent(Struct, kw_only=True):
    check: Check
    result: CheckResult = CheckResult.COMPLETED
    status: int | None = None
    scopes: str | None = None
    error: str | None = None


Observer = Callable[[CheckEvent], None]


class ClientSecretBasic(
    Struct, tag="client_secret_basic", repr_omit_defaults=True
):
    secret: str

    def __repr__(self) -> str:
        return "ClientSecretBasic(<redacted>)"


class PrivateKeyJwt(Struct, tag="private_key_jwt", repr_omit_defaults=True):
    secret: str
    key_id: str | None = None
    algorithm: Literal["RS256", "RS384", "RS512", "PS256", "PS384", "PS512"] = (
        "RS256"
    )
    lifetime_seconds: Annotated[int, Meta(ge=1, le=300)] = 300

    def __repr__(self) -> str:
        return "PrivateKeyJwt(<redacted>)"


def _endpoint(value: str) -> None:
    endpoint = urlsplit(value)
    if (
        endpoint.scheme != "https"
        or not endpoint.hostname
        or endpoint.username is not None
        or endpoint.query
        or endpoint.fragment
        or "%" in endpoint.path
        or any(part in (".", "..") for part in endpoint.path.split("/"))
    ):
        raise ValueError("SMART requires a pinned HTTPS endpoint")


class Verification(Struct, kw_only=True):
    actor_kind: Literal["patient", "practitioner"]
    client_id: Annotated[str, Meta(min_length=1, max_length=256)]
    issuer: Annotated[str, Meta(min_length=1, max_length=2048)]
    fhir_base: Annotated[str, Meta(min_length=1, max_length=2048)]
    jwks_endpoint: Annotated[str, Meta(min_length=1, max_length=2048)]

    def __post_init__(self) -> None:
        for endpoint in (self.issuer, self.fhir_base, self.jwks_endpoint):
            _endpoint(endpoint)


class Login(Struct, kw_only=True):
    verification: Verification
    authorize_endpoint: str
    token_endpoint: str
    callback: str
    authentication: ClientSecretBasic | PrivateKeyJwt | None = None

    def __post_init__(self) -> None:
        for endpoint in (
            self.authorize_endpoint,
            self.token_endpoint,
            self.callback,
        ):
            _endpoint(endpoint)


class TokenError(Struct):
    error: str | None = None


class Identity(Struct, kw_only=True):
    subject: str
    fhir_user: str
    fingerprint: str
    expires_at: int
    actor_kind: Literal["patient", "practitioner"]
    actor_id: str
    actor_name: str
    patient_id: str
    patient_name: str


class VerifiedLaunch(Struct):
    identity: Identity
    tokens: SmartTokens


class RefreshedTokens(Struct, kw_only=True, forbid_unknown_fields=False):
    access_token: Annotated[str, Meta(min_length=1, max_length=16384)]
    token_type: Annotated[str, Meta(pattern="^(?i:bearer)$")]
    expires_in: Annotated[int, Meta(gt=0)]
    scope: Annotated[str, Meta(min_length=1, max_length=4096)]
    refresh_token: (
        Annotated[str, Meta(min_length=1, max_length=16384)] | None
    ) = None

    def __repr__(self) -> str:
        return "RefreshedTokens(<redacted>)"
