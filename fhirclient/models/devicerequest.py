# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceRequest).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_type = "DeviceRequest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn: fhirdatetime.FHIRDateTime | None = None
        """ When recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.codeCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.codeReference: fhirreference.FHIRReference | None = None
        """ Device requested.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter motivating request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier: identifier.Identifier | None = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Request identifier.
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
        
        self.note: list[annotation.Annotation] | None = None
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Desired time or schedule for use.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod: period.Period | None = None
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming: timing.Timing | None = None
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.parameter: list[DeviceRequestParameter] | None = None
        """ Device details.
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """
        
        self.performer: fhirreference.FHIRReference | None = None
        """ Requested Filler.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType: codeableconcept.CodeableConcept | None = None
        """ Filler role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priorRequest: list[fhirreference.FHIRReference] | None = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priority: str | None = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Linked Reason for request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory: list[fhirreference.FHIRReference] | None = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester: fhirreference.FHIRReference | None = None
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Focus of request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo: list[fhirreference.FHIRReference] | None = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.
    
    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    
    resource_type = "DeviceRequestParameter"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Device detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ Value of detail.
        Type `bool`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """
        
        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
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
from . import timing
