# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MoneyQuantity).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Quantity(element.Element):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    
    resource_type = "Quantity"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ Coded form of the unit.
        Type `str`. """
        
        self.comparator: str | None = None
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """
        
        self.system: str | None = None
        """ System that defines coded unit form.
        Type `str`. """
        
        self.unit: str | None = None
        """ Unit representation.
        Type `str`. """
        
        self.value: float | None = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("comparator", "comparator", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("unit", "unit", str, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


