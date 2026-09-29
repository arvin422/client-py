# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Period).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Period(element.Element):
    """ Time range defined by start and end date/time.
    
    A time period defined by a start and end date and optionally time.
    """
    
    resource_type = "Period"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end: fhirdatetime.FHIRDateTime | None = None
        """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.start: fhirdatetime.FHIRDateTime | None = None
        """ Starting time with inclusive boundary.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(Period, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdatetime.FHIRDateTime, False, None, False),
            ("start", "start", fhirdatetime.FHIRDateTime, False, None, False),
        ])
        return js


from . import fhirdatetime
