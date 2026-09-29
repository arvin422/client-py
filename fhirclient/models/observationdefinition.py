# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abnormalCodedValueSet: fhirreference.FHIRReference | None = None
        """ Value set of abnormal coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Category of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticalCodedValueSet: fhirreference.FHIRReference | None = None
        """ Value set of critical coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier for this ObservationDefinition instance.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ Method used to produce the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleResultsAllowed: bool | None = None
        """ Multiple results allowed.
        Type `bool`. """
        
        self.normalCodedValueSet: fhirreference.FHIRReference | None = None
        """ Value set of normal coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.permittedDataType: list[str | None] | None = None
        """ Quantity | CodeableConcept | string | boolean | integer | Range |
        Ratio | SampledData | time | dateTime | Period.
        List of `str` items. """
        
        self.preferredReportName: str | None = None
        """ Preferred report name.
        Type `str`. """
        
        self.qualifiedInterval: list[ObservationDefinitionQualifiedInterval] | None = None
        """ Qualified range for continuous and ordinal observation results.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        
        self.quantitativeDetails: ObservationDefinitionQuantitativeDetails | None = None
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        
        self.validCodedValueSet: fhirreference.FHIRReference | None = None
        """ Value set of valid coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.
    
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    
    resource_type = "ObservationDefinitionQualifiedInterval"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age: range.Range | None = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.appliesTo: list[codeableconcept.CodeableConcept] | None = None
        """ Targetted population of the range.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category: str | None = None
        """ reference | critical | absolute.
        Type `str`. """
        
        self.condition: str | None = None
        """ Condition associated with the reference range.
        Type `str`. """
        
        self.context: codeableconcept.CodeableConcept | None = None
        """ Range context qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.gender: str | None = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.gestationalAge: range.Range | None = None
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.range: range.Range | None = None
        """ The interval itself, for continuous or ordinal observations.
        Type `Range` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", codeableconcept.CodeableConcept, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("range", "range", range.Range, False, None, False),
        ])
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    
    Characteristics for quantitative results of this observation.
    """
    
    resource_type = "ObservationDefinitionQuantitativeDetails"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conversionFactor: float | None = None
        """ SI to Customary unit conversion factor.
        Type `float`. """
        
        self.customaryUnit: codeableconcept.CodeableConcept | None = None
        """ Customary unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decimalPrecision: int | None = None
        """ Decimal precision of observation quantitative results.
        Type `int`. """
        
        self.unit: codeableconcept.CodeableConcept | None = None
        """ SI unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import range
