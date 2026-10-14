"""Async SMART protocol operations without application state or token caches."""

import base64
import hashlib
import hmac
import re
import secrets
from itertools import chain
from typing import TypeVar
from urllib.parse import quote_plus, urlencode, urlsplit

import httpx
import jwt
import msgspec
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

from ._smart_types import (
    Check,
    CheckEvent,
    CheckResult,
    ClientSecretBasic,
    Identity,
    Login,
    Observer,
    OidcHeader,
    OidcKeys,
    PrivateKeyJwt,
    RefreshedTokens,
    SmartClaims,
    SmartDiscovery,
    SmartTokens,
    TokenError,
    Verification,
    VerifiedLaunch,
)
from .async_client import (
    AsyncFHIRClient,
    RequestError,
    ResourceFailure,
    ResourceId,
    SearchFailure,
    Send,
)
from .models.humanname import HumanName
from .models.patient import Patient
from .models.practitioner import Practitioner

T = TypeVar("T")


class InvalidIdentity(ValueError):
    """The supplied evidence does not establish the registered identity."""


class ServiceUnavailable(OSError):
    """A prerequisite read could not be completed."""


class ExchangeUncertain(OSError):
    """A token exchange may have consumed or rotated its credential."""


class TokenRejected(Exception):
    """The token endpoint explicitly rejected an operation."""

    def __init__(self, status: int, code: str | None) -> None:
        self.status = status
        self.code = code
        super().__init__("Token endpoint rejected the request")


def _emit(
    observer: Observer | None,
    check: Check,
    result: CheckResult = CheckResult.COMPLETED,
    *,
    status: int | None = None,
    scopes: str | None = None,
    error: str | None = None,
    resource_failure: ResourceFailure | None = None,
) -> None:
    if observer is not None:
        observer(
            CheckEvent(
                check=check,
                result=result,
                status=status,
                scopes=scopes,
                error=error,
                resource_failure=resource_failure,
            )
        )


def _decode(
    response: httpx.Response,
    kind: type[T],
    check: Check,
    observer: Observer | None,
) -> T:
    if response.status_code != 200:
        _emit(
            observer, check, CheckResult.REJECTED, status=response.status_code
        )
        raise ServiceUnavailable("Protocol read was rejected")
    try:
        if len(response.content) > 65536:
            raise ValueError("Protocol response exceeds size limit")
        value = msgspec.json.decode(response.content, type=kind)
    except (ValueError, msgspec.DecodeError):
        _emit(
            observer, check, CheckResult.REJECTED, status=response.status_code
        )
        raise InvalidIdentity from None
    _emit(observer, check, status=response.status_code)
    return value


def permits(scope: str, permission: str) -> bool:
    """Recognize SMART v1/v2 permissions without widening filtered grants."""
    if "?" in scope:
        return False
    if "/" not in permission:
        return scope == permission
    resource, interaction = permission.rsplit(".", 1)
    context = resource.partition("/")[0]
    received, separator, actions = scope.rpartition(".")
    if not separator or received not in (resource, context + "/*"):
        return False
    actions = {"read": "rs", "write": "cud", "*": "cruds"}.get(actions, actions)
    return bool(actions) and (
        actions == "".join(item for item in "cruds" if item in actions)
        and interaction in actions
    )


def authorization_url(
    config: Login,
    *,
    state: str,
    nonce: str,
    verifier: str,
    scopes: tuple[str, ...],
    launch: str | None = None,
) -> str:
    """Build one authorization request from retained ceremony values."""
    if re.fullmatch(r"[A-Za-z0-9._~-]{43,128}", verifier) is None:
        raise ValueError("Invalid PKCE verifier")
    parameters = {
        "client_id": config.verification.client_id,
        "redirect_uri": config.callback,
        "response_type": "code",
        "scope": " ".join(scopes),
        "state": state,
        "nonce": nonce,
        "aud": config.verification.fhir_base,
        "code_challenge": base64.urlsafe_b64encode(
            hashlib.sha256(verifier.encode("ascii")).digest()
        )
        .decode()
        .rstrip("="),
        "code_challenge_method": "S256",
    }
    if launch is not None:
        parameters["launch"] = launch
    return config.authorize_endpoint + "?" + urlencode(parameters)


async def _token_request(
    config: Login,
    send: Send,
    parameters: dict[str, str],
    now: int,
) -> httpx.Response:
    parameters = {"client_id": config.verification.client_id, **parameters}
    headers = {"accept": "application/json"}
    authentication = config.authentication
    if isinstance(authentication, ClientSecretBasic):
        credentials = (
            quote_plus(config.verification.client_id)
            + ":"
            + quote_plus(authentication.secret)
        )
        headers["authorization"] = (
            "Basic " + base64.b64encode(credentials.encode()).decode()
        )
    elif isinstance(authentication, PrivateKeyJwt):
        claims = {
            "iss": config.verification.client_id,
            "sub": config.verification.client_id,
            "aud": config.token_endpoint,
            "iat": now,
            "exp": now + authentication.lifetime_seconds,
            "jti": secrets.token_hex(32),
        }
        signing_headers = {"alg": authentication.algorithm, "typ": "JWT"}
        if authentication.key_id is not None:
            signing_headers["kid"] = authentication.key_id
        parameters["client_assertion_type"] = (
            "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
        )
        parameters["client_assertion"] = jwt.encode(
            claims,
            authentication.secret,
            algorithm=authentication.algorithm,
            headers=signing_headers,
        )
    try:
        return await send(
            httpx.Request(
                "POST",
                config.token_endpoint,
                data=parameters,
                headers=headers,
            )
        )
    except (OSError, httpx.HTTPError):
        raise ExchangeUncertain from None


def _claims(
    token: str,
    keys: OidcKeys,
    config: Verification,
    nonce: str | None,
    now: int,
    observer: Observer | None,
) -> SmartClaims:
    check = Check.JWT_HEADER
    try:
        header = msgspec.convert(
            jwt.get_unverified_header(token), type=OidcHeader
        )
        if header.b64 is False:
            raise InvalidIdentity
        _emit(observer, check)
        check = Check.JWT_KEY
        candidates = [
            key
            for key in keys.keys
            if header.kid == key.kid
            or (header.kid is None and len(keys.keys) == 1)
        ]
        if len(candidates) != 1:
            raise InvalidIdentity
        candidate = candidates[0]
        if (
            candidate.kty != "RSA"
            or candidate.n is None
            or candidate.e is None
            or candidate.use not in (None, "sig")
            or candidate.alg not in (None, "RS256")
            or (
                candidate.key_ops is not None
                and "verify" not in candidate.key_ops
            )
        ):
            raise InvalidIdentity
        key = jwt.PyJWK.from_dict(
            msgspec.to_builtins(candidate), algorithm="RS256"
        ).key
        if not isinstance(key, RSAPublicKey) or key.key_size < 2048:
            raise InvalidIdentity
        _emit(observer, check)
        check = Check.JWT_CLAIMS
        claims = msgspec.convert(
            jwt.decode(
                token,
                key,
                algorithms=["RS256"],
                audience=config.client_id,
                issuer=config.issuer,
                options={
                    "strict_aud": True,
                    "verify_exp": False,
                    "verify_iat": False,
                    "verify_nbf": False,
                    "require": ["exp", "iat", "sub", "iss", "aud"],
                },
            ),
            type=SmartClaims,
        )
    except (jwt.PyJWTError, ValueError) as error:
        _emit(observer, check, CheckResult.REJECTED, error=type(error).__name__)
        raise InvalidIdentity from None
    _emit(observer, check)
    if (
        claims.exp <= now
        or claims.iat > now + 30
        or (claims.nbf is not None and claims.nbf > now + 30)
    ):
        _emit(observer, Check.JWT_LIFETIME, CheckResult.REJECTED)
        raise InvalidIdentity
    _emit(observer, Check.JWT_LIFETIME)
    if nonce is not None and (
        claims.nonce is None
        or not hmac.compare_digest(claims.nonce.encode(), nonce.encode())
    ):
        _emit(observer, Check.JWT_NONCE, CheckResult.REJECTED)
        raise InvalidIdentity
    _emit(observer, Check.JWT_NONCE)
    return claims


def _name(name: HumanName) -> str:
    return name.text or " ".join(
        filter(None, chain(name.given or [], [name.family]))
    )


def _display(resource: Patient | Practitioner) -> str:
    name = next(filter(bool, map(_name, resource.name or [])), "")
    if not name or len(name) > 256:
        raise InvalidIdentity("FHIR display identity is incomplete")
    return name


async def verify(
    config: Verification,
    tokens: SmartTokens,
    send: Send,
    *,
    nonce: str | None,
    now: int,
    observer: Observer | None = None,
) -> VerifiedLaunch:
    """Verify signed evidence and its independently read FHIR identities."""
    try:
        tokens = msgspec.json.decode(
            msgspec.json.encode(tokens), type=SmartTokens
        )
        if (
            not tokens.access_token.isascii()
            or not tokens.access_token.isprintable()
            or " " in tokens.access_token
        ):
            raise ValueError("Invalid bearer credential")
    except (ValueError, msgspec.DecodeError):
        _emit(observer, Check.TOKEN_RESPONSE, CheckResult.REJECTED)
        raise InvalidIdentity from None
    _emit(observer, Check.TOKEN_RESPONSE, scopes=tokens.scope)
    checks = [
        (Check.SCOPE_OPENID, "openid"),
        (Check.SCOPE_FHIR_USER, "fhirUser"),
        (Check.SCOPE_PATIENT_READ, "patient/Patient.r"),
    ]
    if config.actor_kind == "practitioner":
        checks.append((Check.SCOPE_PRACTITIONER_READ, "user/Practitioner.r"))
    allowed = True
    for check, permission in checks:
        granted = any(
            permits(scope, permission) for scope in tokens.scope.split()
        )
        allowed = allowed and granted
        _emit(
            observer,
            check,
            CheckResult.COMPLETED if granted else CheckResult.REJECTED,
        )
    if not allowed:
        raise InvalidIdentity
    try:
        response = await send(httpx.Request("GET", config.jwks_endpoint))
        keys = _decode(response, OidcKeys, Check.JWKS_RESPONSE, observer)
    except (OSError, httpx.HTTPError):
        raise ServiceUnavailable from None
    claims = _claims(tokens.id_token, keys, config, nonce, now, observer)
    digest = (
        base64.urlsafe_b64encode(
            hashlib.sha256(tokens.access_token.encode()).digest()[:16]
        )
        .decode()
        .rstrip("=")
    )
    if claims.at_hash is not None and not hmac.compare_digest(
        claims.at_hash, digest
    ):
        _emit(observer, Check.ACCESS_TOKEN_HASH, CheckResult.REJECTED)
        raise InvalidIdentity
    _emit(observer, Check.ACCESS_TOKEN_HASH)
    user = claims.fhir_user.removeprefix(config.fhir_base.rstrip("/") + "/")
    kind, separator, identifier = user.partition("/")
    expected = "Patient" if config.actor_kind == "patient" else "Practitioner"
    try:
        identifier = msgspec.convert(identifier, type=ResourceId)
        if (
            kind != expected
            or not separator
            or (kind == "Patient" and identifier != tokens.patient)
        ):
            raise InvalidIdentity
    except ValueError:
        _emit(observer, Check.FHIR_USER, CheckResult.REJECTED)
        raise InvalidIdentity from None
    _emit(observer, Check.FHIR_USER)
    base = urlsplit(config.fhir_base)

    async def authorized(request: httpx.Request) -> httpx.Response:
        target = urlsplit(str(request.url))
        if (
            (target.scheme, target.netloc) != (base.scheme, base.netloc)
            or not target.path.startswith(base.path.rstrip("/") + "/")
            or target.username is not None
            or target.fragment
        ):
            raise InvalidIdentity
        request.headers["authorization"] = "Bearer " + tokens.access_token
        return await send(request)

    fhir = AsyncFHIRClient(config.fhir_base, authorized)
    check = Check.FHIR_ACTOR_RESPONSE
    try:
        actor = await fhir.read(
            Patient if config.actor_kind == "patient" else Practitioner,
            identifier,
        )
        _emit(observer, check, status=200)
        if isinstance(actor, Patient):
            patient = actor
        else:
            check = Check.FHIR_PATIENT_RESPONSE
            patient = await fhir.read(Patient, tokens.patient)
            _emit(observer, check, status=200)
    except RequestError as error:
        _emit(
            observer,
            check,
            CheckResult.REJECTED,
            status=error.status,
            resource_failure=error.failure,
        )
        if error.reason is SearchFailure.MALFORMED:
            raise InvalidIdentity from None
        raise ServiceUnavailable from None
    identity = Identity(
        subject=claims.sub,
        fhir_user=config.fhir_base.rstrip("/") + "/" + user,
        fingerprint=hashlib.sha256(tokens.id_token.encode()).hexdigest(),
        expires_at=claims.exp,
        actor_kind=config.actor_kind,
        actor_id=identifier,
        actor_name=_display(actor),
        patient_id=tokens.patient,
        patient_name=_display(patient),
    )
    _emit(observer, Check.FHIR_IDENTITY)
    return VerifiedLaunch(identity, tokens)


async def exchange(
    config: Login,
    send: Send,
    *,
    code: str,
    verifier: str,
    nonce: str,
    now: int,
    observer: Observer | None = None,
) -> VerifiedLaunch:
    """Exchange a consumed code once and verify its retained nonce."""
    _emit(observer, Check.DISCOVERY_RESPONSE, CheckResult.AWAITING)
    try:
        response = await send(
            httpx.Request(
                "GET",
                config.verification.fhir_base.rstrip("/")
                + "/.well-known/smart-configuration",
            )
        )
    except (OSError, httpx.HTTPError):
        raise ServiceUnavailable from None
    discovery = _decode(
        response, SmartDiscovery, Check.DISCOVERY_RESPONSE, observer
    )
    if (
        discovery.authorization_endpoint != config.authorize_endpoint
        or discovery.token_endpoint != config.token_endpoint
    ):
        _emit(observer, Check.DISCOVERY_ENDPOINTS, CheckResult.REJECTED)
        raise InvalidIdentity
    _emit(observer, Check.DISCOVERY_ENDPOINTS)
    _emit(observer, Check.TOKEN_EXCHANGE, CheckResult.AWAITING)
    try:
        response = await _token_request(
            config,
            send,
            {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": config.callback,
                "code_verifier": verifier,
            },
            now,
        )
    except ExchangeUncertain:
        _emit(observer, Check.TOKEN_EXCHANGE, CheckResult.UNCONFIRMED)
        raise
    _emit(
        observer,
        Check.TOKEN_EXCHANGE,
        CheckResult.COMPLETED
        if response.status_code == 200
        else CheckResult.REJECTED,
        status=response.status_code,
    )
    if response.status_code in (400, 401, 403):
        raise InvalidIdentity
    if response.status_code != 200:
        raise ExchangeUncertain
    tokens = _decode(response, SmartTokens, Check.TOKEN_RESPONSE, observer)
    return await verify(
        config.verification,
        tokens,
        send,
        nonce=nonce,
        now=now,
        observer=observer,
    )


def _token_error(response: httpx.Response) -> TokenRejected:
    code = None
    try:
        if len(response.content) <= 65536:
            value = msgspec.json.decode(response.content, type=TokenError).error
            if value in (
                "invalid_request",
                "invalid_client",
                "invalid_grant",
                "unauthorized_client",
                "unsupported_grant_type",
                "invalid_scope",
                "temporarily_unavailable",
                "server_error",
            ):
                code = value
    except msgspec.DecodeError:
        pass
    return TokenRejected(response.status_code, code)


async def refresh(
    config: Login, send: Send, *, refresh_token: str, now: int
) -> RefreshedTokens:
    """Rotate once; the caller owns durable claims and credential retention."""
    response = await _token_request(
        config,
        send,
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        now,
    )
    if response.status_code != 200:
        raise _token_error(response)
    try:
        if len(response.content) > 65536:
            raise ValueError
        return msgspec.json.decode(response.content, type=RefreshedTokens)
    except (ValueError, msgspec.DecodeError):
        raise ExchangeUncertain from None


async def revoke(
    config: Login, send: Send, *, endpoint: str, token: str, now: int
) -> None:
    """Revoke one credential through an explicitly configured endpoint."""
    request = msgspec.structs.replace(config, token_endpoint=endpoint)
    response = await _token_request(
        request,
        send,
        {
            "token": token,
            "token_type_hint": "refresh_token",
        },
        now,
    )
    if response.status_code >= 400 and response.status_code != 404:
        raise _token_error(response)


__all__ = [
    "Check",
    "CheckEvent",
    "CheckResult",
    "ClientSecretBasic",
    "ExchangeUncertain",
    "InvalidIdentity",
    "Login",
    "PrivateKeyJwt",
    "RefreshedTokens",
    "ResourceFailure",
    "ServiceUnavailable",
    "SmartTokens",
    "TokenRejected",
    "Verification",
    "VerifiedLaunch",
    "authorization_url",
    "exchange",
    "permits",
    "refresh",
    "revoke",
    "verify",
]
