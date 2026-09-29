# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VerificationResult).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class VerificationResult(domainresource.DomainResource):
    """ Describes validation requirements, source(s), status and dates for one or
    more elements.
    """
    
    resource_type = "VerificationResult"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attestation: VerificationResultAttestation | None = None
        """ Information about the entity attesting to information.
        Type `VerificationResultAttestation` (represented as `dict` in JSON). """
        
        self.failureAction: codeableconcept.CodeableConcept | None = None
        """ fatal | warn | rec-only | none.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequency: timing.Timing | None = None
        """ Frequency of revalidation.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.lastPerformed: fhirdatetime.FHIRDateTime | None = None
        """ The date/time validation was last completed (including failed
        validations).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.need: codeableconcept.CodeableConcept | None = None
        """ none | initial | periodic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.nextScheduled: fhirdate.FHIRDate | None = None
        """ The date when target is next validated, if appropriate.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.primarySource: list[VerificationResultPrimarySource] | None = None
        """ Information about the primary source(s) involved in validation.
        List of `VerificationResultPrimarySource` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ attested | validated | in-process | req-revalid | val-fail | reval-
        fail.
        Type `str`. """
        
        self.statusDate: fhirdatetime.FHIRDateTime | None = None
        """ When the validation status was updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.target: list[fhirreference.FHIRReference] | None = None
        """ A resource that was validated.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetLocation: list[str | None] | None = None
        """ The fhirpath location(s) within the resource that was validated.
        List of `str` items. """
        
        self.validationProcess: list[codeableconcept.CodeableConcept] | None = None
        """ The primary process by which the target is validated (edit check;
        value set; primary source; multiple sources; standalone; in
        context).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationType: codeableconcept.CodeableConcept | None = None
        """ nothing | primary | multiple.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validator: list[VerificationResultValidator] | None = None
        """ Information about the entity validating information.
        List of `VerificationResultValidator` items (represented as `dict` in JSON). """
        
        super(VerificationResult, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(VerificationResult, self).elementProperties()
        js.extend([
            ("attestation", "attestation", VerificationResultAttestation, False, None, False),
            ("failureAction", "failureAction", codeableconcept.CodeableConcept, False, None, False),
            ("frequency", "frequency", timing.Timing, False, None, False),
            ("lastPerformed", "lastPerformed", fhirdatetime.FHIRDateTime, False, None, False),
            ("need", "need", codeableconcept.CodeableConcept, False, None, False),
            ("nextScheduled", "nextScheduled", fhirdate.FHIRDate, False, None, False),
            ("primarySource", "primarySource", VerificationResultPrimarySource, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, False),
            ("targetLocation", "targetLocation", str, True, None, False),
            ("validationProcess", "validationProcess", codeableconcept.CodeableConcept, True, None, False),
            ("validationType", "validationType", codeableconcept.CodeableConcept, False, None, False),
            ("validator", "validator", VerificationResultValidator, True, None, False),
        ])
        return js


from . import backboneelement

class VerificationResultAttestation(backboneelement.BackboneElement):
    """ Information about the entity attesting to information.
    """
    
    resource_type = "VerificationResultAttestation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.communicationMethod: codeableconcept.CodeableConcept | None = None
        """ The method by which attested information was submitted/retrieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date: fhirdate.FHIRDate | None = None
        """ The date the information was attested to.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onBehalfOf: fhirreference.FHIRReference | None = None
        """ When the who is asserting on behalf of another (organization or
        individual).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.proxyIdentityCertificate: str | None = None
        """ A digital identity certificate associated with the proxy entity
        submitting attested information on behalf of the attestation source.
        Type `str`. """
        
        self.proxySignature: signature.Signature | None = None
        """ Proxy signature.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.sourceIdentityCertificate: str | None = None
        """ A digital identity certificate associated with the attestation
        source.
        Type `str`. """
        
        self.sourceSignature: signature.Signature | None = None
        """ Attester signature.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.who: fhirreference.FHIRReference | None = None
        """ The individual or organization attesting to information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(VerificationResultAttestation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(VerificationResultAttestation, self).elementProperties()
        js.extend([
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("proxyIdentityCertificate", "proxyIdentityCertificate", str, False, None, False),
            ("proxySignature", "proxySignature", signature.Signature, False, None, False),
            ("sourceIdentityCertificate", "sourceIdentityCertificate", str, False, None, False),
            ("sourceSignature", "sourceSignature", signature.Signature, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class VerificationResultPrimarySource(backboneelement.BackboneElement):
    """ Information about the primary source(s) involved in validation.
    """
    
    resource_type = "VerificationResultPrimarySource"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.canPushUpdates: codeableconcept.CodeableConcept | None = None
        """ yes | no | undetermined.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.communicationMethod: list[codeableconcept.CodeableConcept] | None = None
        """ Method for exchanging information with the primary source.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.pushTypeAvailable: list[codeableconcept.CodeableConcept] | None = None
        """ specific | any | source.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Type of primary source (License Board; Primary Education;
        Continuing Education; Postal Service; Relationship owner;
        Registration Authority; legal source; issuing source; authoritative
        source).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.validationDate: fhirdatetime.FHIRDateTime | None = None
        """ When the target was validated against the primary source.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.validationStatus: codeableconcept.CodeableConcept | None = None
        """ successful | failed | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.who: fhirreference.FHIRReference | None = None
        """ Reference to the primary source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(VerificationResultPrimarySource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(VerificationResultPrimarySource, self).elementProperties()
        js.extend([
            ("canPushUpdates", "canPushUpdates", codeableconcept.CodeableConcept, False, None, False),
            ("communicationMethod", "communicationMethod", codeableconcept.CodeableConcept, True, None, False),
            ("pushTypeAvailable", "pushTypeAvailable", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("validationDate", "validationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("validationStatus", "validationStatus", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class VerificationResultValidator(backboneelement.BackboneElement):
    """ Information about the entity validating information.
    """
    
    resource_type = "VerificationResultValidator"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attestationSignature: signature.Signature | None = None
        """ Validator signature.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.identityCertificate: str | None = None
        """ A digital identity certificate associated with the validator.
        Type `str`. """
        
        self.organization: fhirreference.FHIRReference | None = None
        """ Reference to the organization validating information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(VerificationResultValidator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(VerificationResultValidator, self).elementProperties()
        js.extend([
            ("attestationSignature", "attestationSignature", signature.Signature, False, None, False),
            ("identityCertificate", "identityCertificate", str, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import signature
from . import timing
