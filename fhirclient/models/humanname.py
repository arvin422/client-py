# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HumanName).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
    """
    
    resource_type = "HumanName"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.family: str | None = None
        """ Family name (often called 'Surname').
        Type `str`. """
        
        self.given: list[str | None] | None = None
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """
        
        self.period: period.Period | None = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.prefix: list[str | None] | None = None
        """ Parts that come before the name.
        List of `str` items. """
        
        self.suffix: list[str | None] | None = None
        """ Parts that come after the name.
        List of `str` items. """
        
        self.text: str | None = None
        """ Text representation of the full name.
        Type `str`. """
        
        self.use: str | None = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, False, None, False),
            ("given", "given", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("text", "text", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import period
