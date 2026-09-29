# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    
    resource_type = "FamilyMemberHistory"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageAge: age.Age | None = None
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.ageRange: range.Range | None = None
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString: str | None = None
        """ (approximate) age.
        Type `str`. """
        
        self.bornDate: fhirdate.FHIRDate | None = None
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornPeriod: period.Period | None = None
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornString: str | None = None
        """ (approximate) date of birth.
        Type `str`. """
        
        self.condition: list[FamilyMemberHistoryCondition] | None = None
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason: codeableconcept.CodeableConcept | None = None
        """ subject-unknown | withheld | unable-to-obtain | deferred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ When history was recorded or last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.deceasedAge: age.Age | None = None
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """
        
        self.deceasedBoolean: bool | None = None
        """ Dead? How old/when?.
        Type `bool`. """
        
        self.deceasedDate: fhirdate.FHIRDate | None = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedRange: range.Range | None = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString: str | None = None
        """ Dead? How old/when?.
        Type `str`. """
        
        self.estimatedAge: bool | None = None
        """ Age is estimated?.
        Type `bool`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: list[str | None] | None = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri: list[str | None] | None = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.name: str | None = None
        """ The family member described.
        Type `str`. """
        
        self.note: list[annotation.Annotation] | None = None
        """ General note about related person.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Patient history is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Why was family member history performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why was family member history performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relationship: codeableconcept.CodeableConcept | None = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sex: codeableconcept.CodeableConcept | None = None
        """ male | female | other | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", age.Age, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False, "born", False),
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("deceasedAge", "deceasedAge", age.Age, False, "deceased", False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False, "deceased", False),
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True),
            ("sex", "sex", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_type = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contributedToDeath: bool | None = None
        """ Whether the condition contributed to the cause of death.
        Type `bool`. """
        
        self.note: list[annotation.Annotation] | None = None
        """ Extra information about condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge: age.Age | None = None
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetPeriod: period.Period | None = None
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange: range.Range | None = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString: str | None = None
        """ When condition first manifested.
        Type `str`. """
        
        self.outcome: codeableconcept.CodeableConcept | None = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import age
from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range
