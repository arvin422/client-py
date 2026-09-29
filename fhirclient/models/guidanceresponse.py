# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    
    resource_type = "GuidanceResponse"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dataRequirement: list[datarequirement.DataRequirement] | None = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter during which the response was returned.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.evaluationMessage: list[fhirreference.FHIRReference] | None = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.moduleCanonical: str | None = None
        """ What guidance was requested.
        Type `str`. """
        
        self.moduleCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ What guidance was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.moduleUri: str | None = None
        """ What guidance was requested.
        Type `str`. """
        
        self.note: list[annotation.Annotation] | None = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When the guidance response was processed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.outputParameters: fhirreference.FHIRReference | None = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer: fhirreference.FHIRReference | None = None
        """ Device returning the guidance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Why guidance is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why guidance is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requestIdentifier: identifier.Identifier | None = None
        """ The identifier of the request associated with this response, if any.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.result: fhirreference.FHIRReference | None = None
        """ Proposed actions, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Patient the request was performed for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import datarequirement
from . import fhirdatetime
from . import fhirreference
from . import identifier
