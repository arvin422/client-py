# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Address).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    
    resource_type = "Address"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.city: str | None = None
        """ Name of city, town etc..
        Type `str`. """
        
        self.country: str | None = None
        """ Country (e.g. can be ISO 3166 2 or 3 letter code).
        Type `str`. """
        
        self.district: str | None = None
        """ District name (aka county).
        Type `str`. """
        
        self.line: list[str | None] | None = None
        """ Street name, number, direction & P.O. Box etc..
        List of `str` items. """
        
        self.period: period.Period | None = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.postalCode: str | None = None
        """ Postal code for area.
        Type `str`. """
        
        self.state: str | None = None
        """ Sub-unit of country (abbreviations ok).
        Type `str`. """
        
        self.text: str | None = None
        """ Text representation of the address.
        Type `str`. """
        
        self.type: str | None = None
        """ postal | physical | both.
        Type `str`. """
        
        self.use: str | None = None
        """ home | work | temp | old | billing - purpose of this address.
        Type `str`. """
        
        super(Address, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, False, None, False),
            ("country", "country", str, False, None, False),
            ("district", "district", str, False, None, False),
            ("line", "line", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import period
