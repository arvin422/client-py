# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Population).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import backboneelement

class Population(backboneelement.BackboneElement):
    """ A definition of a set of people that apply to some clinically related
    context, for example people contraindicated for a certain medication.
    
    A populatioof people with some set of grouping criteria.
    """
    
    resource_type = "Population"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ The age of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ageRange: range.Range | None = None
        """ The age of the specific population.
        Type `Range` (represented as `dict` in JSON). """
        
        self.gender: codeableconcept.CodeableConcept | None = None
        """ The gender of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.physiologicalCondition: codeableconcept.CodeableConcept | None = None
        """ The existing physiological conditions of the specific population to
        which this applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.race: codeableconcept.CodeableConcept | None = None
        """ Race of the specific population.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Population, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Population, self).elementProperties()
        js.extend([
            ("ageCodeableConcept", "ageCodeableConcept", codeableconcept.CodeableConcept, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("gender", "gender", codeableconcept.CodeableConcept, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", codeableconcept.CodeableConcept, False, None, False),
            ("race", "race", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import range
