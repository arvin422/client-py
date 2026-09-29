# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    
    A kind of specimen with associated set of requirements.
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection: list[codeableconcept.CodeableConcept] | None = None
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patientPreparation: list[codeableconcept.CodeableConcept] | None = None
        """ Patient preparation for collection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.timeAspect: str | None = None
        """ Time aspect for collection.
        Type `str`. """
        
        self.typeCollected: codeableconcept.CodeableConcept | None = None
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.typeTested: list[SpecimenDefinitionTypeTested] | None = None
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patientPreparation", "patientPreparation", codeableconcept.CodeableConcept, True, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
        ])
        return js


from . import backboneelement

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    
    Specimen conditioned in a container as expected by the testing laboratory.
    """
    
    resource_type = "SpecimenDefinitionTypeTested"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.container: SpecimenDefinitionTypeTestedContainer | None = None
        """ The specimen's container.
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """
        
        self.handling: list[SpecimenDefinitionTypeTestedHandling] | None = None
        """ Specimen handling before testing.
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """
        
        self.isDerived: bool | None = None
        """ Primary or secondary specimen.
        Type `bool`. """
        
        self.preference: str | None = None
        """ preferred | alternate.
        Type `str`. """
        
        self.rejectionCriterion: list[codeableconcept.CodeableConcept] | None = None
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requirement: str | None = None
        """ Specimen requirements.
        Type `str`. """
        
        self.retentionTime: duration.Duration | None = None
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTested, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
            ("isDerived", "isDerived", bool, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive: list[SpecimenDefinitionTypeTestedContainerAdditive] | None = None
        """ Additive associated with container.
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """
        
        self.cap: codeableconcept.CodeableConcept | None = None
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.capacity: quantity.Quantity | None = None
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Container description.
        Type `str`. """
        
        self.material: codeableconcept.CodeableConcept | None = None
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.minimumVolumeQuantity: quantity.Quantity | None = None
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minimumVolumeString: str | None = None
        """ Minimum volume.
        Type `str`. """
        
        self.preparation: str | None = None
        """ Specimen container preparation.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("minimumVolumeQuantity", "minimumVolumeQuantity", quantity.Quantity, False, "minimumVolume", False),
            ("minimumVolumeString", "minimumVolumeString", str, False, "minimumVolume", False),
            ("preparation", "preparation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainerAdditive"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference: fhirreference.FHIRReference | None = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
        ])
        return js


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedHandling"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction: str | None = None
        """ Preservation instruction.
        Type `str`. """
        
        self.maxDuration: duration.Duration | None = None
        """ Maximum preservation time.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.temperatureQualifier: codeableconcept.CodeableConcept | None = None
        """ Temperature qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.temperatureRange: range.Range | None = None
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(SpecimenDefinitionTypeTestedHandling, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False),
            ("temperatureRange", "temperatureRange", range.Range, False, None, False),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import range
