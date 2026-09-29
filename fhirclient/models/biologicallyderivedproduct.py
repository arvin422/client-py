# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.
    
    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """
    
    resource_type = "BiologicallyDerivedProduct"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection: BiologicallyDerivedProductCollection | None = None
        """ How this product was collected.
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.manipulation: BiologicallyDerivedProductManipulation | None = None
        """ Any manipulation of product post-collection.
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """
        
        self.parent: list[fhirreference.FHIRReference] | None = None
        """ BiologicallyDerivedProduct parent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.processing: list[BiologicallyDerivedProductProcessing] | None = None
        """ Any processing of the product during collection.
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """
        
        self.productCategory: str | None = None
        """ organ | tissue | fluid | cells | biologicalAgent.
        Type `str`. """
        
        self.productCode: codeableconcept.CodeableConcept | None = None
        """ What this biologically derived product is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity: int | None = None
        """ The amount of this biologically derived product.
        Type `int`. """
        
        self.request: list[fhirreference.FHIRReference] | None = None
        """ Procedure request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ available | unavailable.
        Type `str`. """
        
        self.storage: list[BiologicallyDerivedProductStorage] | None = None
        """ Product storage.
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js


from . import backboneelement

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """
    
    resource_type = "BiologicallyDerivedProductCollection"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collectedDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Time of product collection.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.collectedPeriod: period.Period | None = None
        """ Time of product collection.
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector: fhirreference.FHIRReference | None = None
        """ Individual performing collection.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source: fhirreference.FHIRReference | None = None
        """ Who is product from.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", fhirdatetime.FHIRDateTime, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.
    
    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """
    
    resource_type = "BiologicallyDerivedProductManipulation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Description of manipulation.
        Type `str`. """
        
        self.timeDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Time of manipulation.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timePeriod: period.Period | None = None
        """ Time of manipulation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductManipulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdatetime.FHIRDateTime, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.
    
    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """
    
    resource_type = "BiologicallyDerivedProductProcessing"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive: fhirreference.FHIRReference | None = None
        """ Substance added during processing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Description of of processing.
        Type `str`. """
        
        self.procedure: codeableconcept.CodeableConcept | None = None
        """ Procesing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timeDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Time of processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timePeriod: period.Period | None = None
        """ Time of processing.
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdatetime.FHIRDateTime, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """
    
    resource_type = "BiologicallyDerivedProductStorage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Description of storage.
        Type `str`. """
        
        self.duration: period.Period | None = None
        """ Storage timeperiod.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scale: str | None = None
        """ farenheit | celsius | kelvin.
        Type `str`. """
        
        self.temperature: float | None = None
        """ Storage temperature.
        Type `float`. """
        
        super(BiologicallyDerivedProductStorage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("temperature", "temperature", float, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
