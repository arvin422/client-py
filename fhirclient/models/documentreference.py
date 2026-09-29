# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentReference).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.
    
    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """
    
    resource_type = "DocumentReference"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authenticator: fhirreference.FHIRReference | None = None
        """ Who/what authenticated the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.author: list[fhirreference.FHIRReference] | None = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Categorization of document.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.content: list[DocumentReferenceContent] | None = None
        """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """
        
        self.context: DocumentReferenceContext | None = None
        """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        
        self.custodian: fhirreference.FHIRReference | None = None
        """ Organization which maintains the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date: fhirinstant.FHIRInstant | None = None
        """ When this document reference was created.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.description: str | None = None
        """ Human-readable description.
        Type `str`. """
        
        self.docStatus: str | None = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.masterIdentifier: identifier.Identifier | None = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relatesTo: list[DocumentReferenceRelatesTo] | None = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.securityLabel: list[codeableconcept.CodeableConcept] | None = None
        """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ current | superseded | entered-in-error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Who/what is the subject of the document.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("content", "content", DocumentReferenceContent, True, None, True),
            ("context", "context", DocumentReferenceContext, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirinstant.FHIRInstant, False, None, False),
            ("description", "description", str, False, None, False),
            ("docStatus", "docStatus", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True, None, False),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.
    
    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """
    
    resource_type = "DocumentReferenceContent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment: attachment.Attachment | None = None
        """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.format: coding.Coding | None = None
        """ Format/content rules for the document.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, True),
            ("format", "format", coding.Coding, False, None, False),
        ])
        return js


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.
    
    The clinical context in which the document was prepared.
    """
    
    resource_type = "DocumentReferenceContext"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.encounter: list[fhirreference.FHIRReference] | None = None
        """ Context of the document  content.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.event: list[codeableconcept.CodeableConcept] | None = None
        """ Main clinical acts documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.facilityType: codeableconcept.CodeableConcept | None = None
        """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """
        
        self.practiceSetting: codeableconcept.CodeableConcept | None = None
        """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.related: list[fhirreference.FHIRReference] | None = None
        """ Related identifiers or resources.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sourcePatientInfo: fhirreference.FHIRReference | None = None
        """ Patient demographics from source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("event", "event", codeableconcept.CodeableConcept, True, None, False),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False, None, False),
            ("related", "related", fhirreference.FHIRReference, True, None, False),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.
    
    Relationships that this document has with other document references that
    already exist.
    """
    
    resource_type = "DocumentReferenceRelatesTo"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ replaces | transforms | signs | appends.
        Type `str`. """
        
        self.target: fhirreference.FHIRReference | None = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceRelatesTo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period
