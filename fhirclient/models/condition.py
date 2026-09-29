# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Condition).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.
    
    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    
    resource_type = "Condition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abatementAge: age.Age | None = None
        """ When in resolution/remission.
        Type `Age` (represented as `dict` in JSON). """
        
        self.abatementDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When in resolution/remission.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.abatementPeriod: period.Period | None = None
        """ When in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.abatementRange: range.Range | None = None
        """ When in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
        
        self.abatementString: str | None = None
        """ When in resolution/remission.
        Type `str`. """
        
        self.asserter: fhirreference.FHIRReference | None = None
        """ Person who asserts this condition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.bodySite: list[codeableconcept.CodeableConcept] | None = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ problem-list-item | encounter-diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.clinicalStatus: codeableconcept.CodeableConcept | None = None
        """ active | recurrence | relapse | inactive | remission | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.evidence: list[ConditionEvidence] | None = None
        """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Additional information about the Condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge: age.Age | None = None
        """ Estimated or actual date,  date-time, or age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.onsetPeriod: period.Period | None = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange: range.Range | None = None
        """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString: str | None = None
        """ Estimated or actual date,  date-time, or age.
        Type `str`. """
        
        self.recordedDate: fhirdatetime.FHIRDateTime | None = None
        """ Date record was first recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recorder: fhirreference.FHIRReference | None = None
        """ Who recorded the condition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.severity: codeableconcept.CodeableConcept | None = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stage: list[ConditionStage] | None = None
        """ Stage/grade, usually assessed formally.
        List of `ConditionStage` items (represented as `dict` in JSON). """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who has the condition?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.verificationStatus: codeableconcept.CodeableConcept | None = None
        """ unconfirmed | provisional | differential | confirmed | refuted |
        entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Condition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", fhirdatetime.FHIRDateTime, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", period.Period, False, "abatement", False),
            ("abatementRange", "abatementRange", range.Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdatetime.FHIRDateTime, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    
    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    
    resource_type = "ConditionEvidence"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: list[codeableconcept.CodeableConcept] | None = None
        """ Manifestation/symptom.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail: list[fhirreference.FHIRReference] | None = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.
    
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    
    resource_type = "ConditionStage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment: list[fhirreference.FHIRReference] | None = None
        """ Formal record of assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.summary: codeableconcept.CodeableConcept | None = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of staging.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
