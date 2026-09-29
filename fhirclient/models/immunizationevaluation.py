# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ImmunizationEvaluation(domainresource.DomainResource):
    """ Immunization evaluation information.
    
    Describes a comparison of an immunization event against published
    recommendations to determine if the administration is "valid" in relation
    to those  recommendations.
    """
    
    resource_type = "ImmunizationEvaluation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority: fhirreference.FHIRReference | None = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date evaluation was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description: str | None = None
        """ Evaluation notes.
        Type `str`. """
        
        self.doseNumberPositiveInt: int | None = None
        """ Dose number within series.
        Type `int`. """
        
        self.doseNumberString: str | None = None
        """ Dose number within series.
        Type `str`. """
        
        self.doseStatus: codeableconcept.CodeableConcept | None = None
        """ Status of the dose relative to published recommendations.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason: list[codeableconcept.CodeableConcept] | None = None
        """ Reason for the dose status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.immunizationEvent: fhirreference.FHIRReference | None = None
        """ Immunization being evaluated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who this evaluation is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.series: str | None = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDosesPositiveInt: int | None = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.seriesDosesString: str | None = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self.status: str | None = None
        """ completed | entered-in-error.
        Type `str`. """
        
        self.targetDisease: codeableconcept.CodeableConcept | None = None
        """ Evaluation target disease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("status", "status", str, False, None, True),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
