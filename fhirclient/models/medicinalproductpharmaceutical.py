# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    
    resource_type = "MedicinalProductPharmaceutical"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administrableDoseForm: codeableconcept.CodeableConcept | None = None
        """ The administrable dose form, after necessary reconstitution.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.characteristics: list[MedicinalProductPharmaceuticalCharacteristics] | None = None
        """ Characteristics e.g. a products onset of action.
        List of `MedicinalProductPharmaceuticalCharacteristics` items (represented as `dict` in JSON). """
        
        self.device: list[fhirreference.FHIRReference] | None = None
        """ Accompanying device.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ An identifier for the pharmaceutical medicinal product.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient: list[fhirreference.FHIRReference] | None = None
        """ Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.routeOfAdministration: list[MedicinalProductPharmaceuticalRouteOfAdministration] | None = None
        """ The path by which the pharmaceutical product is taken into or makes
        contact with the body.
        List of `MedicinalProductPharmaceuticalRouteOfAdministration` items (represented as `dict` in JSON). """
        
        self.unitOfPresentation: codeableconcept.CodeableConcept | None = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceutical, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    
    resource_type = "MedicinalProductPharmaceuticalCharacteristics"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ A coded characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status: codeableconcept.CodeableConcept | None = None
        """ The status of characteristic e.g. assigned or pending.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministration(backboneelement.BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministration"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Coded expression for the route.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.firstDose: quantity.Quantity | None = None
        """ The first dose (dose quantity) administered in humans can be
        specified, for a product under investigation, using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerDay: quantity.Quantity | None = None
        """ The maximum dose per day (maximum dose quantity to be administered
        in any one 24-h period) that can be administered as per the
        protocol referenced in the clinical trial authorisation.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerTreatmentPeriod: ratio.Ratio | None = None
        """ The maximum dose per treatment period that can be administered as
        per the protocol referenced in the clinical trial authorisation.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxSingleDose: quantity.Quantity | None = None
        """ The maximum single dose that can be administered as per the
        protocol of a clinical trial can be specified using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxTreatmentPeriod: duration.Duration | None = None
        """ The maximum treatment period during which an Investigational
        Medicinal Product can be administered as per the protocol
        referenced in the clinical trial authorisation.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.targetSpecies: list[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies] | None = None
        """ A species for which this route applies.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("firstDose", "firstDose", quantity.Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False),
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False),
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ A species for which this route applies.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Coded expression for the species.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.withdrawalPeriod: list[MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod] | None = None
        """ A species specific time during which consumption of animal product
        is not appropriate.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    
    resource_type = "MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.supportingInformation: str | None = None
        """ Extra information about the withdrawal period.
        Type `str`. """
        
        self.tissue: codeableconcept.CodeableConcept | None = None
        """ Coded expression for the type of tissue for which the withdrawal
        period applues, e.g. meat, milk.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: quantity.Quantity | None = None
        """ A value for the time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("supportingInformation", "supportingInformation", str, False, None, False),
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, True),
        ])
        return js


from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
