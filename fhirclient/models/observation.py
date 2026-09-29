# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Observation).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Observation(domainresource.DomainResource):
    """ Measurements and simple assertions.
    
    Measurements and simple assertions made about a patient, device or other
    subject.
    """
    
    resource_type = "Observation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Classification of  type of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.component: list[ObservationComponent] | None = None
        """ Component results.
        List of `ObservationComponent` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason: codeableconcept.CodeableConcept | None = None
        """ Why the result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.derivedFrom: list[fhirreference.FHIRReference] | None = None
        """ Related measurements the observation is made from.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device: fhirreference.FHIRReference | None = None
        """ (Measurement) Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.effectiveDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Clinically relevant time/time-period for observation.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.effectiveInstant: fhirinstant.FHIRInstant | None = None
        """ Clinically relevant time/time-period for observation.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.effectivePeriod: period.Period | None = None
        """ Clinically relevant time/time-period for observation.
        Type `Period` (represented as `dict` in JSON). """
        
        self.effectiveTiming: timing.Timing | None = None
        """ Clinically relevant time/time-period for observation.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Healthcare event during which this observation is made.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focus: list[fhirreference.FHIRReference] | None = None
        """ What the observation is about, when it is not about the subject of
        record.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.hasMember: list[fhirreference.FHIRReference] | None = None
        """ Related resource that belongs to the Observation group.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for observation.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpretation: list[codeableconcept.CodeableConcept] | None = None
        """ High, low, normal, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.issued: fhirinstant.FHIRInstant | None = None
        """ Date/Time this version was made available.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ How it was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments about the observation.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf: list[fhirreference.FHIRReference] | None = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performer: list[fhirreference.FHIRReference] | None = None
        """ Who is responsible for the observation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.referenceRange: list[ObservationReferenceRange] | None = None
        """ Provides guide for interpretation.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.specimen: fhirreference.FHIRReference | None = None
        """ Specimen used for this observation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ registered | preliminary | final | amended +.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who and/or what the observation is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ Actual result.
        Type `bool`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Actual result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Actual result.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Actual result.
        Type `int`. """
        
        self.valuePeriod: period.Period | None = None
        """ Actual result.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Actual result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Actual result.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio: ratio.Ratio | None = None
        """ Actual result.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData: sampleddata.SampledData | None = None
        """ Actual result.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Actual result.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Actual result.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        super(Observation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Observation, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("component", "component", ObservationComponent, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", False),
            ("effectiveInstant", "effectiveInstant", fhirinstant.FHIRInstant, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("effectiveTiming", "effectiveTiming", timing.Timing, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("hasMember", "hasMember", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("issued", "issued", fhirinstant.FHIRInstant, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", False),
        ])
        return js


from . import backboneelement

class ObservationComponent(backboneelement.BackboneElement):
    """ Component results.
    
    Some observations have multiple component observations.  These component
    observations are expressed as separate code value pairs that share the same
    attributes.  Examples include systolic and diastolic component observations
    for blood pressure measurement and multiple component observations for
    genetics observations.
    """
    
    resource_type = "ObservationComponent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Type of component observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dataAbsentReason: codeableconcept.CodeableConcept | None = None
        """ Why the component result is missing.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interpretation: list[codeableconcept.CodeableConcept] | None = None
        """ High, low, normal, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.referenceRange: list[ObservationReferenceRange] | None = None
        """ Provides guide for interpretation of component result.
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ Actual component result.
        Type `bool`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Actual component result.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Actual component result.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Actual component result.
        Type `int`. """
        
        self.valuePeriod: period.Period | None = None
        """ Actual component result.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Actual component result.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Actual component result.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio: ratio.Ratio | None = None
        """ Actual component result.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData: sampleddata.SampledData | None = None
        """ Actual component result.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Actual component result.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Actual component result.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        super(ObservationComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", False),
        ])
        return js


class ObservationReferenceRange(backboneelement.BackboneElement):
    """ Provides guide for interpretation.
    
    Guidance on how to interpret the value by comparison to a normal or
    recommended range.  Multiple reference ranges are interpreted as an "OR".
    In other words, to represent two distinct target populations, two
    `referenceRange` elements would be used.
    """
    
    resource_type = "ObservationReferenceRange"
    
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
        """ Reference range population.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.high: quantity.Quantity | None = None
        """ High Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.low: quantity.Quantity | None = None
        """ Low Range, if relevant.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Text based reference range in an observation.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Reference range qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationReferenceRange, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import timing
