# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    
    resource_type = "ImmunizationRecommendation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority: fhirreference.FHIRReference | None = None
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date recommendation(s) created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recommendation: list[ImmunizationRecommendationRecommendation] | None = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    
    resource_type = "ImmunizationRecommendationRecommendation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindicatedVaccineCode: list[codeableconcept.CodeableConcept] | None = None
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateCriterion: list[ImmunizationRecommendationRecommendationDateCriterion] | None = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Protocol details.
        Type `str`. """
        
        self.doseNumberPositiveInt: int | None = None
        """ Recommended dose number within series.
        Type `int`. """
        
        self.doseNumberString: str | None = None
        """ Recommended dose number within series.
        Type `str`. """
        
        self.forecastReason: list[codeableconcept.CodeableConcept] | None = None
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.forecastStatus: codeableconcept.CodeableConcept | None = None
        """ Vaccine recommendation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series: str | None = None
        """ Name of vaccination series.
        Type `str`. """
        
        self.seriesDosesPositiveInt: int | None = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.seriesDosesString: str | None = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self.supportingImmunization: list[fhirreference.FHIRReference] | None = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingPatientInformation: list[fhirreference.FHIRReference] | None = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetDisease: codeableconcept.CodeableConcept | None = None
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.vaccineCode: list[codeableconcept.CodeableConcept] | None = None
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    resource_type = "ImmunizationRecommendationRecommendationDateCriterion"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: fhirdatetime.FHIRDateTime | None = None
        """ Recommended date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", fhirdatetime.FHIRDateTime, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
