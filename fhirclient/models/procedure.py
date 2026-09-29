# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Procedure).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter: fhirreference.FHIRReference | None = None
        """ Person who asserts this procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ A request for this procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite: list[codeableconcept.CodeableConcept] | None = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.complication: list[codeableconcept.CodeableConcept] | None = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail: list[fhirreference.FHIRReference] | None = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focalDevice: list[ProcedureFocalDevice] | None = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.followUp: list[codeableconcept.CodeableConcept] | None = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: list[str | None] | None = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri: list[str | None] | None = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.location: fhirreference.FHIRReference | None = None
        """ Where the procedure happened.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome: codeableconcept.CodeableConcept | None = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.partOf: list[fhirreference.FHIRReference] | None = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performedAge: age.Age | None = None
        """ When the procedure was performed.
        Type `Age` (represented as `dict` in JSON). """
        
        self.performedDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.performedPeriod: period.Period | None = None
        """ When the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performedRange: range.Range | None = None
        """ When the procedure was performed.
        Type `Range` (represented as `dict` in JSON). """
        
        self.performedString: str | None = None
        """ When the procedure was performed.
        Type `str`. """
        
        self.performer: list[ProcedurePerformer] | None = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorder: fhirreference.FHIRReference | None = None
        """ Who recorded the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.report: list[fhirreference.FHIRReference] | None = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        
        self.statusReason: codeableconcept.CodeableConcept | None = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who the procedure was performed on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.usedCode: list[codeableconcept.CodeableConcept] | None = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.usedReference: list[fhirreference.FHIRReference] | None = None
        """ Items used during procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performedAge", "performedAge", age.Age, False, "performed", False),
            ("performedDateTime", "performedDateTime", fhirdatetime.FHIRDateTime, False, "performed", False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("performedRange", "performedRange", range.Range, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    
    resource_type = "ProcedureFocalDevice"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: codeableconcept.CodeableConcept | None = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated: fhirreference.FHIRReference | None = None
        """ Device that was changed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to "real" people rather than equipment.
    """
    
    resource_type = "ProcedurePerformer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor: fhirreference.FHIRReference | None = None
        """ The reference to the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function: codeableconcept.CodeableConcept | None = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.onBehalfOf: fhirreference.FHIRReference | None = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import age
from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range
