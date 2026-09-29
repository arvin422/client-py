# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/UsageContext).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class UsageContext(element.Element):
    """ Describes the context of use for a conformance or knowledge resource.
    
    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """
    
    resource_type = "UsageContext"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: coding.Coding | None = None
        """ Type of context being specified.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Value that defines the context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Value that defines the context.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Value that defines the context.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Value that defines the context.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirreference
from . import quantity
from . import range
