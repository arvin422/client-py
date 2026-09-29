# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_type = "MedicationAdministration"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context: fhirreference.FHIRReference | None = None
        """ Encounter or Episode of Care administered as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.device: list[fhirreference.FHIRReference] | None = None
        """ Device used to administer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.dosage: MedicationAdministrationDosage | None = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.effectiveDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Start and end time of administration.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.effectivePeriod: period.Period | None = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.eventHistory: list[fhirreference.FHIRReference] | None = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiates: list[str | None] | None = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        
        self.medicationCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference: fhirreference.FHIRReference | None = None
        """ What was administered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Information about the administration.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf: list[fhirreference.FHIRReference] | None = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performer: list[MedicationAdministrationPerformer] | None = None
        """ Who performed the medication administration and what they did.
        List of `MedicationAdministrationPerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Condition or observation that supports why the medication was
        administered.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.request: fhirreference.FHIRReference | None = None
        """ Request administration performed against.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ in-progress | not-done | on-hold | completed | entered-in-error |
        stopped | unknown.
        Type `str`. """
        
        self.statusReason: list[codeableconcept.CodeableConcept] | None = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who received medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInformation: list[fhirreference.FHIRReference] | None = None
        """ Additional information to support administration.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", True),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", True),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    
    resource_type = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dose: quantity.Quantity | None = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rateQuantity: quantity.Quantity | None = None
        """ Dose quantity per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio: ratio.Ratio | None = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route: codeableconcept.CodeableConcept | None = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site: codeableconcept.CodeableConcept | None = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ Who performed the medication administration and what they did.
    
    Indicates who or what performed the medication administration and how they
    were involved.
    """
    
    resource_type = "MedicationAdministrationPerformer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor: fhirreference.FHIRReference | None = None
        """ Who performed the medication administration.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function: codeableconcept.CodeableConcept | None = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationAdministrationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import ratio
