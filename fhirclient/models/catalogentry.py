# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CatalogEntry).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.
    
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    
    resource_type = "CatalogEntry"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalCharacteristic: list[codeableconcept.CodeableConcept] | None = None
        """ Additional characteristics of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalClassification: list[codeableconcept.CodeableConcept] | None = None
        """ Additional classification of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalIdentifier: list[identifier.Identifier] | None = None
        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.classification: list[codeableconcept.CodeableConcept] | None = None
        """ Classification (category or class) of the item entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Unique identifier of the catalog item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastUpdated: fhirdatetime.FHIRDateTime | None = None
        """ When was this catalog last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.orderable: bool | None = None
        """ Whether the entry represents an orderable item.
        Type `bool`. """
        
        self.referencedItem: fhirreference.FHIRReference | None = None
        """ The item that is being defined.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relatedEntry: list[CatalogEntryRelatedEntry] | None = None
        """ An item that this catalog entry is related to.
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ The type of item - medication, device, service, protocol or other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validTo: fhirdatetime.FHIRDateTime | None = None
        """ The date until which this catalog entry is expected to be active.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.validityPeriod: period.Period | None = None
        """ The time period in which this catalog entry is expected to be
        active.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastUpdated", "lastUpdated", fhirdatetime.FHIRDateTime, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("validTo", "validTo", fhirdatetime.FHIRDateTime, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


from . import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.
    
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    
    resource_type = "CatalogEntryRelatedEntry"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item: fhirreference.FHIRReference | None = None
        """ The reference to the related item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationtype: str | None = None
        """ triggers | is-replaced-by.
        Type `str`. """
        
        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", fhirreference.FHIRReference, False, None, True),
            ("relationtype", "relationtype", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
