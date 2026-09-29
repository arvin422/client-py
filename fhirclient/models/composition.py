# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Composition).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Composition(domainresource.DomainResource):
    """ A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    
    A set of healthcare-related information that is assembled together into a
    single logical package that provides a single coherent statement of
    meaning, establishes its own context and that has clinical attestation with
    regard to who is making the statement. A Composition defines the structure
    and narrative content necessary for a document. However, a Composition
    alone does not constitute a document. Rather, the Composition must be the
    first entry in a Bundle where Bundle.type=document, and any other resources
    referenced from Composition must be included as subsequent entries in the
    Bundle (for example Patient, Practitioner, Encounter, etc.).
    """
    
    resource_type = "Composition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attester: list[CompositionAttester] | None = None
        """ Attests to accuracy of composition.
        List of `CompositionAttester` items (represented as `dict` in JSON). """
        
        self.author: list[fhirreference.FHIRReference] | None = None
        """ Who and/or what authored the composition.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Categorization of Composition.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.confidentiality: str | None = None
        """ As defined by affinity domain.
        Type `str`. """
        
        self.custodian: fhirreference.FHIRReference | None = None
        """ Organization which maintains the composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Composition editing time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Context of the Composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.event: list[CompositionEvent] | None = None
        """ The clinical service(s) being documented.
        List of `CompositionEvent` items (represented as `dict` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Version-independent identifier for the Composition.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relatesTo: list[CompositionRelatesTo] | None = None
        """ Relationships to other compositions/documents.
        List of `CompositionRelatesTo` items (represented as `dict` in JSON). """
        
        self.section: list[CompositionSection] | None = None
        """ Composition is broken into sections.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who and/or what the composition is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Human Readable name/title.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of composition (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Composition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Composition, self).elementProperties()
        js.extend([
            ("attester", "attester", CompositionAttester, True, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("confidentiality", "confidentiality", str, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", CompositionEvent, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("relatesTo", "relatesTo", CompositionRelatesTo, True, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class CompositionAttester(backboneelement.BackboneElement):
    """ Attests to accuracy of composition.
    
    A participant who has attested to the accuracy of the composition/document.
    """
    
    resource_type = "CompositionAttester"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode: str | None = None
        """ personal | professional | legal | official.
        Type `str`. """
        
        self.party: fhirreference.FHIRReference | None = None
        """ Who attested the composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.time: fhirdatetime.FHIRDateTime | None = None
        """ When the composition was attested.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(CompositionAttester, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CompositionAttester, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, True),
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("time", "time", fhirdatetime.FHIRDateTime, False, None, False),
        ])
        return js


class CompositionEvent(backboneelement.BackboneElement):
    """ The clinical service(s) being documented.
    
    The clinical service, such as a colonoscopy or an appendectomy, being
    documented.
    """
    
    resource_type = "CompositionEvent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: list[codeableconcept.CodeableConcept] | None = None
        """ Code(s) that apply to the event being documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail: list[fhirreference.FHIRReference] | None = None
        """ The event(s) being documented.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ The period covered by the documentation.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CompositionEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CompositionEvent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


class CompositionRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.
    
    Relationships that this composition has with other compositions or
    documents that already exist.
    """
    
    resource_type = "CompositionRelatesTo"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ replaces | transforms | signs | appends.
        Type `str`. """
        
        self.targetIdentifier: identifier.Identifier | None = None
        """ Target of the relationship.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.targetReference: fhirreference.FHIRReference | None = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CompositionRelatesTo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CompositionRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
        ])
        return js


class CompositionSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.
    
    The root of the sections that make up the composition.
    """
    
    resource_type = "CompositionSection"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author: list[fhirreference.FHIRReference] | None = None
        """ Who and/or what authored the section.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.emptyReason: codeableconcept.CodeableConcept | None = None
        """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entry: list[fhirreference.FHIRReference] | None = None
        """ A reference to data that supports this section.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.focus: fhirreference.FHIRReference | None = None
        """ Who/what the section is about, when it is not about the subject of
        composition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.mode: str | None = None
        """ working | snapshot | changes.
        Type `str`. """
        
        self.orderedBy: codeableconcept.CodeableConcept | None = None
        """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.section: list[CompositionSection] | None = None
        """ Nested Section.
        List of `CompositionSection` items (represented as `dict` in JSON). """
        
        self.text: narrative.Narrative | None = None
        """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Label for section (e.g. for ToC).
        Type `str`. """
        
        super(CompositionSection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CompositionSection, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("entry", "entry", fhirreference.FHIRReference, True, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("section", "section", CompositionSection, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import narrative
from . import period
