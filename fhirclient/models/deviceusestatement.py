# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.derivedFrom: list[fhirreference.FHIRReference] | None = None
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device: fhirreference.FHIRReference | None = None
        """ Reference to device used.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Addition details (comments, instructions).
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why was DeviceUseStatement performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recordedOn: fhirdatetime.FHIRDateTime | None = None
        """ When statement was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.source: fhirreference.FHIRReference | None = None
        """ Who made the statement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | completed | entered-in-error +.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Patient using device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingDateTime: fhirdatetime.FHIRDateTime | None = None
        """ How often  the device was used.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timingPeriod: period.Period | None = None
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming: timing.Timing | None = None
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recordedOn", "recordedOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdatetime.FHIRDateTime, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import timing
