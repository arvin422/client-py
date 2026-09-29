# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Dosage).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import backboneelement

class Dosage(backboneelement.BackboneElement):
    """ How the medication is/was taken or should be taken.
    
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    
    resource_type = "Dosage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalInstruction: list[codeableconcept.CodeableConcept] | None = None
        """ Supplemental instruction or warnings to the patient - e.g. "with
        meals", "may cause drowsiness".
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.asNeededBoolean: bool | None = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseAndRate: list[DosageDoseAndRate] | None = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        
        self.maxDosePerAdministration: quantity.Quantity | None = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerLifetime: quantity.Quantity | None = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod: ratio.Ratio | None = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patientInstruction: str | None = None
        """ Patient or consumer oriented instructions.
        Type `str`. """
        
        self.route: codeableconcept.CodeableConcept | None = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ The order of the dosage instructions.
        Type `int`. """
        
        self.site: codeableconcept.CodeableConcept | None = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        
        self.timing: timing.Timing | None = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
        ])
        return js


from . import element

class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.
    
    The amount of medication administered.
    """
    
    resource_type = "DosageDoseAndRate"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity: quantity.Quantity | None = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.doseRange: range.Range | None = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateQuantity: quantity.Quantity | None = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRange: range.Range | None = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio: ratio.Ratio | None = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ The kind of dose or rate specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import quantity
from . import range
from . import ratio
from . import timing
