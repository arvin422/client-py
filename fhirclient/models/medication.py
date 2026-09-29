# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Medication).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    
    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    
    resource_type = "Medication"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount: ratio.Ratio | None = None
        """ Amount of drug in package.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.batch: MedicationBatch | None = None
        """ Details about packaged medications.
        Type `MedicationBatch` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.form: codeableconcept.CodeableConcept | None = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier for this medication.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient: list[MedicationIngredient] | None = None
        """ Active or inactive ingredient.
        List of `MedicationIngredient` items (represented as `dict` in JSON). """
        
        self.manufacturer: fhirreference.FHIRReference | None = None
        """ Manufacturer of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        
        super(Medication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Medication, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, False, None, False),
            ("batch", "batch", MedicationBatch, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", MedicationIngredient, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    resource_type = "MedicationBatch"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expirationDate: fhirdatetime.FHIRDateTime | None = None
        """ When batch will expire.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.lotNumber: str | None = None
        """ Identifier assigned to batch.
        Type `str`. """
        
        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
        ])
        return js


class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_type = "MedicationIngredient"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isActive: bool | None = None
        """ Active ingredient indicator.
        Type `bool`. """
        
        self.itemCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ The actual ingredient or content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference: fhirreference.FHIRReference | None = None
        """ The actual ingredient or content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.strength: ratio.Ratio | None = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("strength", "strength", ratio.Ratio, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import ratio
