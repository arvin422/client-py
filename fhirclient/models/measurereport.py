# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MeasureReport).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ Results of a measure evaluation.
    
    The MeasureReport resource contains the results of the calculation of a
    measure; and optionally a reference to the resources involved in that
    calculation.
    """
    
    resource_type = "MeasureReport"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ When the report was generated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.evaluatedResource: list[fhirreference.FHIRReference] | None = None
        """ What data was used to calculate the measure score.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.group: list[MeasureReportGroup] | None = None
        """ Measure results for each group.
        List of `MeasureReportGroup` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Additional identifier for the MeasureReport.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.improvementNotation: codeableconcept.CodeableConcept | None = None
        """ increase | decrease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.measure: str | None = None
        """ What measure was calculated.
        Type `str`. """
        
        self.period: period.Period | None = None
        """ What period the report covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.reporter: fhirreference.FHIRReference | None = None
        """ Who is reporting the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ complete | pending | error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ What individual(s) the report is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: str | None = None
        """ individual | subject-list | summary | data-collection.
        Type `str`. """
        
        super(MeasureReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("evaluatedResource", "evaluatedResource", fhirreference.FHIRReference, True, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("measure", "measure", str, False, None, True),
            ("period", "period", period.Period, False, None, True),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class MeasureReportGroup(backboneelement.BackboneElement):
    """ Measure results for each group.
    
    The results of the calculation, one for each population group in the
    measure.
    """
    
    resource_type = "MeasureReportGroup"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Meaning of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.measureScore: quantity.Quantity | None = None
        """ What score this group achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.population: list[MeasureReportGroupPopulation] | None = None
        """ The populations in the group.
        List of `MeasureReportGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier: list[MeasureReportGroupStratifier] | None = None
        """ Stratification results.
        List of `MeasureReportGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
        ])
        return js


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
    """ The populations in the group.
    
    The populations that make up the population group, one for each type of
    population appropriate for the measure.
    """
    
    resource_type = "MeasureReportGroupPopulation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.count: int | None = None
        """ Size of the population.
        Type `int`. """
        
        self.subjectResults: fhirreference.FHIRReference | None = None
        """ For subject-list reports, the subject results in this population.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ Stratification results.
    
    When a measure includes multiple stratifiers, there will be a stratifier
    group for each stratifier defined by the measure.
    """
    
    resource_type = "MeasureReportGroupStratifier"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: list[codeableconcept.CodeableConcept] | None = None
        """ What stratifier of the group.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.stratum: list[MeasureReportGroupStratifierStratum] | None = None
        """ Stratum results, one for each unique value, or set of values, in
        the stratifier, or stratifier components.
        List of `MeasureReportGroupStratifierStratum` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ Stratum results, one for each unique value, or set of values, in the
    stratifier, or stratifier components.
    
    This element contains the results for a single stratum within the
    stratifier. For example, when stratifying on administrative gender, there
    will be four strata, one for each possible gender value.
    """
    
    resource_type = "MeasureReportGroupStratifierStratum"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component: list[MeasureReportGroupStratifierStratumComponent] | None = None
        """ Stratifier component values.
        List of `MeasureReportGroupStratifierStratumComponent` items (represented as `dict` in JSON). """
        
        self.measureScore: quantity.Quantity | None = None
        """ What score this stratum achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.population: list[MeasureReportGroupStratifierStratumPopulation] | None = None
        """ Population results in this stratum.
        List of `MeasureReportGroupStratifierStratumPopulation` items (represented as `dict` in JSON). """
        
        self.value: codeableconcept.CodeableConcept | None = None
        """ The stratum value, e.g. male.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratum, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("component", "component", MeasureReportGroupStratifierStratumComponent, True, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("value", "value", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ Stratifier component values.
    
    A stratifier component value.
    """
    
    resource_type = "MeasureReportGroupStratifierStratumComponent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ What stratifier component of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: codeableconcept.CodeableConcept | None = None
        """ The stratum component value, e.g. male.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratumComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ Population results in this stratum.
    
    The populations that make up the stratum, one for each type of population
    appropriate to the measure.
    """
    
    resource_type = "MeasureReportGroupStratifierStratumPopulation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.count: int | None = None
        """ Size of the population.
        Type `int`. """
        
        self.subjectResults: fhirreference.FHIRReference | None = None
        """ For subject-list reports, the subject results in this population.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratumPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
