# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SampledData).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.
    
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    
    resource_type = "SampledData"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data: str | None = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """
        
        self.dimensions: int | None = None
        """ Number of sample points at each time point.
        Type `int`. """
        
        self.factor: float | None = None
        """ Multiply data by this before adding to origin.
        Type `float`. """
        
        self.lowerLimit: float | None = None
        """ Lower limit of detection.
        Type `float`. """
        
        self.origin: quantity.Quantity | None = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.period: float | None = None
        """ Number of milliseconds between samples.
        Type `float`. """
        
        self.upperLimit: float | None = None
        """ Upper limit of detection.
        Type `float`. """
        
        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("factor", "factor", float, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("upperLimit", "upperLimit", float, False, None, False),
        ])
        return js


from . import quantity
