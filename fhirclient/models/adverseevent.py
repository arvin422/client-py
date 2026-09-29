# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AdverseEvent).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.
    
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    
    resource_type = "AdverseEvent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actuality: str | None = None
        """ actual | potential.
        Type `str`. """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ product-problem | product-quality | product-use-error | wrong-dose
        | incorrect-prescribing-information | wrong-technique | wrong-
        route-of-administration | wrong-rate | wrong-duration | wrong-time
        | expired-drug | medical-device-use-error | problem-different-
        manufacturer | unsafe-physical-environment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contributor: list[fhirreference.FHIRReference] | None = None
        """ Who  was involved in the adverse event or the potential adverse
        event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ When the event occurred.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.detected: fhirdatetime.FHIRDateTime | None = None
        """ When the event was detected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.event: codeableconcept.CodeableConcept | None = None
        """ Type of the event itself in relation to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Business identifier for the event.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.location: fhirreference.FHIRReference | None = None
        """ Location where adverse event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome: codeableconcept.CodeableConcept | None = None
        """ resolved | recovering | ongoing | resolvedWithSequelae | fatal |
        unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recordedDate: fhirdatetime.FHIRDateTime | None = None
        """ When the event was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recorder: fhirreference.FHIRReference | None = None
        """ Who recorded the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceDocument: list[fhirreference.FHIRReference] | None = None
        """ AdverseEvent.referenceDocument.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.resultingCondition: list[fhirreference.FHIRReference] | None = None
        """ Effect on the subject due to this event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.seriousness: codeableconcept.CodeableConcept | None = None
        """ Seriousness of the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity: codeableconcept.CodeableConcept | None = None
        """ mild | moderate | severe.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.study: list[fhirreference.FHIRReference] | None = None
        """ AdverseEvent.study.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Subject impacted by event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subjectMedicalHistory: list[fhirreference.FHIRReference] | None = None
        """ AdverseEvent.subjectMedicalHistory.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.suspectEntity: list[AdverseEventSuspectEntity] | None = None
        """ The suspected agent causing the adverse event.
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """
        
        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("detected", "detected", fhirdatetime.FHIRDateTime, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("referenceDocument", "referenceDocument", fhirreference.FHIRReference, True, None, False),
            ("resultingCondition", "resultingCondition", fhirreference.FHIRReference, True, None, False),
            ("seriousness", "seriousness", codeableconcept.CodeableConcept, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("study", "study", fhirreference.FHIRReference, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("subjectMedicalHistory", "subjectMedicalHistory", fhirreference.FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
        ])
        return js


from . import backboneelement

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.
    
    Describes the entity that is suspected to have caused the adverse event.
    """
    
    resource_type = "AdverseEventSuspectEntity"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.causality: list[AdverseEventSuspectEntityCausality] | None = None
        """ Information on the possible cause of the event.
        List of `AdverseEventSuspectEntityCausality` items (represented as `dict` in JSON). """
        
        self.instance: fhirreference.FHIRReference | None = None
        """ Refers to the specific entity that caused the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AdverseEventSuspectEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """ Information on the possible cause of the event.
    """
    
    resource_type = "AdverseEventSuspectEntityCausality"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment: codeableconcept.CodeableConcept | None = None
        """ Assessment of if the entity caused the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author: fhirreference.FHIRReference | None = None
        """ AdverseEvent.suspectEntity.causalityAuthor.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ ProbabilityScale | Bayesian | Checklist.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productRelatedness: str | None = None
        """ AdverseEvent.suspectEntity.causalityProductRelatedness.
        Type `str`. """
        
        super(AdverseEventSuspectEntityCausality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", codeableconcept.CodeableConcept, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
