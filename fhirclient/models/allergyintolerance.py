# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_type = "AllergyIntolerance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter: fhirreference.FHIRReference | None = None
        """ Source of the information about the allergy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category: list[str | None] | None = None
        """ food | medication | environment | biologic.
        List of `str` items. """
        
        self.clinicalStatus: codeableconcept.CodeableConcept | None = None
        """ active | inactive | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Code that identifies the allergy or intolerance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticality: str | None = None
        """ low | high | unable-to-assess.
        Type `str`. """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter when the allergy or intolerance was asserted.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastOccurrence: fhirdatetime.FHIRDateTime | None = None
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Additional text not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge: age.Age | None = None
        """ When allergy or intolerance was identified.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When allergy or intolerance was identified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.onsetPeriod: period.Period | None = None
        """ When allergy or intolerance was identified.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange: range.Range | None = None
        """ When allergy or intolerance was identified.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString: str | None = None
        """ When allergy or intolerance was identified.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who the sensitivity is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reaction: list[AllergyIntoleranceReaction] | None = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        
        self.recordedDate: fhirdatetime.FHIRDateTime | None = None
        """ Date first version of the resource instance was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recorder: fhirreference.FHIRReference | None = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: str | None = None
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `str`. """
        
        self.verificationStatus: codeableconcept.CodeableConcept | None = None
        """ unconfirmed | confirmed | refuted | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("category", "category", str, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdatetime.FHIRDateTime, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdatetime.FHIRDateTime, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    
    resource_type = "AllergyIntoleranceReaction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Description of the event as a whole.
        Type `str`. """
        
        self.exposureRoute: codeableconcept.CodeableConcept | None = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation: list[codeableconcept.CodeableConcept] | None = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Text about event not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onset: fhirdatetime.FHIRDateTime | None = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.severity: str | None = None
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """
        
        self.substance: codeableconcept.CodeableConcept | None = None
        """ Specific substance or pharmaceutical product considered to be
        responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onset", "onset", fhirdatetime.FHIRDateTime, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
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
