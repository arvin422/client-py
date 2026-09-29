# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ServiceRequest).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.
    
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    
    resource_type = "ServiceRequest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asNeededBoolean: bool | None = None
        """ Preconditions for service.
        Type `bool`. """
        
        self.asNeededCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Preconditions for service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authoredOn: fhirdatetime.FHIRDateTime | None = None
        """ Date request signed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite: list[codeableconcept.CodeableConcept] | None = None
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Classification of service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doNotPerform: bool | None = None
        """ True if service/procedure should not be performed.
        Type `bool`. """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter in which the request was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: list[str | None] | None = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri: list[str | None] | None = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.insurance: list[fhirreference.FHIRReference] | None = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent: str | None = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """
        
        self.locationCode: list[codeableconcept.CodeableConcept] | None = None
        """ Requested location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.locationReference: list[fhirreference.FHIRReference] | None = None
        """ Requested location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When service should occur.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod: period.Period | None = None
        """ When service should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming: timing.Timing | None = None
        """ When service should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.orderDetail: list[codeableconcept.CodeableConcept] | None = None
        """ Additional order information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientInstruction: str | None = None
        """ Patient or consumer-oriented instructions.
        Type `str`. """
        
        self.performer: list[fhirreference.FHIRReference] | None = None
        """ Requested performer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType: codeableconcept.CodeableConcept | None = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priority: str | None = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.quantityQuantity: quantity.Quantity | None = None
        """ Service amount.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantityRange: range.Range | None = None
        """ Service amount.
        Type `Range` (represented as `dict` in JSON). """
        
        self.quantityRatio: ratio.Ratio | None = None
        """ Service amount.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Explanation/Justification for procedure or service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Explanation/Justification for service or service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory: list[fhirreference.FHIRReference] | None = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces: list[fhirreference.FHIRReference] | None = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester: fhirreference.FHIRReference | None = None
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requisition: identifier.Identifier | None = None
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.specimen: list[fhirreference.FHIRReference] | None = None
        """ Procedure Samples.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Individual or Entity the service is ordered for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo: list[fhirreference.FHIRReference] | None = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing
