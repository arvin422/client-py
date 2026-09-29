# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Timing).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import backboneelement

class Timing(backboneelement.BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    
    resource_type = "Timing"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ BID | TID | QID | AM | PM | QD | QOD | +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event: list[fhirdatetime.FHIRDateTime | None] | None = None
        """ When the event occurs.
        List of `FHIRDateTime` items (represented as `str` in JSON). """
        
        self.repeat: TimingRepeat | None = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("event", "event", fhirdatetime.FHIRDateTime, True, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
        ])
        return js


from . import element

class TimingRepeat(element.Element):
    """ When the event is to occur.
    
    A set of rules that describe when the event is scheduled.
    """
    
    resource_type = "TimingRepeat"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsDuration: duration.Duration | None = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.boundsPeriod: period.Period | None = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """
        
        self.boundsRange: range.Range | None = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """
        
        self.count: int | None = None
        """ Number of times to repeat.
        Type `int`. """
        
        self.countMax: int | None = None
        """ Maximum number of times to repeat.
        Type `int`. """
        
        self.dayOfWeek: list[str | None] | None = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self.duration: float | None = None
        """ How long when it happens.
        Type `float`. """
        
        self.durationMax: float | None = None
        """ How long when it happens (Max).
        Type `float`. """
        
        self.durationUnit: str | None = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.frequency: int | None = None
        """ Event occurs frequency times per period.
        Type `int`. """
        
        self.frequencyMax: int | None = None
        """ Event occurs up to frequencyMax times per period.
        Type `int`. """
        
        self.offset: int | None = None
        """ Minutes from event (before or after).
        Type `int`. """
        
        self.period: float | None = None
        """ Event occurs frequency times per period.
        Type `float`. """
        
        self.periodMax: float | None = None
        """ Upper limit of period (3-4 hours).
        Type `float`. """
        
        self.periodUnit: str | None = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.timeOfDay: list[fhirtime.FHIRTime | None] | None = None
        """ Time of day for action.
        List of `FHIRTime` items (represented as `str` in JSON). """
        
        self.when: list[str | None] | None = None
        """ Code for time period of occurrence.
        List of `str` items. """
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", duration.Duration, False, "bounds", False),
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False),
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False),
            ("count", "count", int, False, None, False),
            ("countMax", "countMax", int, False, None, False),
            ("dayOfWeek", "dayOfWeek", str, True, None, False),
            ("duration", "duration", float, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("durationUnit", "durationUnit", str, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("period", "period", float, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("periodUnit", "periodUnit", str, False, None, False),
            ("timeOfDay", "timeOfDay", fhirtime.FHIRTime, True, None, False),
            ("when", "when", str, True, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirdatetime
from . import fhirtime
from . import period
from . import range
