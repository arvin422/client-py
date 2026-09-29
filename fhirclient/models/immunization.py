# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Immunization).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity: quantity.Quantity | None = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.education: list[ImmunizationEducation] | None = None
        """ Educational material presented to patient.
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter immunization was part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.expirationDate: fhirdate.FHIRDate | None = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fundingSource: codeableconcept.CodeableConcept | None = None
        """ Funding source for the vaccine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.isSubpotent: bool | None = None
        """ Dose potency.
        Type `bool`. """
        
        self.location: fhirreference.FHIRReference | None = None
        """ Where immunization occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber: str | None = None
        """ Vaccine lot number.
        Type `str`. """
        
        self.manufacturer: fhirreference.FHIRReference | None = None
        """ Vaccine manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Additional immunization notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Vaccine administration date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrenceString: str | None = None
        """ Vaccine administration date.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who was immunized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer: list[ImmunizationPerformer] | None = None
        """ Who performed event.
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """
        
        self.primarySource: bool | None = None
        """ Indicates context the data was recorded in.
        Type `bool`. """
        
        self.programEligibility: list[codeableconcept.CodeableConcept] | None = None
        """ Patient eligibility for a vaccination program.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.protocolApplied: list[ImmunizationProtocolApplied] | None = None
        """ Protocol followed by the provider.
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """
        
        self.reaction: list[ImmunizationReaction] | None = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why immunization occurred.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorded: fhirdatetime.FHIRDateTime | None = None
        """ When the immunization was first captured in the subject's record.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.reportOrigin: codeableconcept.CodeableConcept | None = None
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route: codeableconcept.CodeableConcept | None = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site: codeableconcept.CodeableConcept | None = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ completed | entered-in-error | not-done.
        Type `str`. """
        
        self.statusReason: codeableconcept.CodeableConcept | None = None
        """ Reason not done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subpotentReason: list[codeableconcept.CodeableConcept] | None = None
        """ Reason for being subpotent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.vaccineCode: codeableconcept.CodeableConcept | None = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorded", "recorded", fhirdatetime.FHIRDateTime, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.
    
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    
    resource_type = "ImmunizationEducation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentType: str | None = None
        """ Educational material document identifier.
        Type `str`. """
        
        self.presentationDate: fhirdatetime.FHIRDateTime | None = None
        """ Educational material presentation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publicationDate: fhirdatetime.FHIRDateTime | None = None
        """ Educational material publication date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.reference: str | None = None
        """ Educational material reference pointer.
        Type `str`. """
        
        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("presentationDate", "presentationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("publicationDate", "publicationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who performed the immunization event.
    """
    
    resource_type = "ImmunizationPerformer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor: fhirreference.FHIRReference | None = None
        """ Individual or organization who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function: codeableconcept.CodeableConcept | None = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.
    
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    
    resource_type = "ImmunizationProtocolApplied"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority: fhirreference.FHIRReference | None = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.doseNumberPositiveInt: int | None = None
        """ Dose number within series.
        Type `int`. """
        
        self.doseNumberString: str | None = None
        """ Dose number within series.
        Type `str`. """
        
        self.series: str | None = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDosesPositiveInt: int | None = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.seriesDosesString: str | None = None
        """ Recommended number of doses for immunity.
        Type `str`. """
        
        self.targetDisease: list[codeableconcept.CodeableConcept] | None = None
        """ Vaccine preventatable disease being targetted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationProtocolApplied, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    resource_type = "ImmunizationReaction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ When reaction started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.detail: fhirreference.FHIRReference | None = None
        """ Additional information on reaction.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reported: bool | None = None
        """ Indicates self-reported reaction.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
