# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Library).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.
    
    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """
    
    resource_type = "Library"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate: fhirdate.FHIRDate | None = None
        """ When the library was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author: list[contactdetail.ContactDetail] | None = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.contact: list[contactdetail.ContactDetail] | None = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.content: list[attachment.Attachment] | None = None
        """ Contents of the library, either embedded or referenced.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.copyright: str | None = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.dataRequirement: list[datarequirement.DataRequirement] | None = None
        """ What data is referenced by this library.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description: str | None = None
        """ Natural language description of the library.
        Type `str`. """
        
        self.editor: list[contactdetail.ContactDetail] | None = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod: period.Period | None = None
        """ When the library is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser: list[contactdetail.ContactDetail] | None = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Additional identifier for the library.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for library (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate: fhirdate.FHIRDate | None = None
        """ When the library was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name: str | None = None
        """ Name for this library (computer friendly).
        Type `str`. """
        
        self.parameter: list[parameterdefinition.ParameterDefinition] | None = None
        """ Parameters defined by the library.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose: str | None = None
        """ Why this library is defined.
        Type `str`. """
        
        self.relatedArtifact: list[relatedartifact.RelatedArtifact] | None = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer: list[contactdetail.ContactDetail] | None = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subjectCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Type of individual the library content is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference: fhirreference.FHIRReference | None = None
        """ Type of individual the library content is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subtitle: str | None = None
        """ Subordinate title of the library.
        Type `str`. """
        
        self.title: str | None = None
        """ Name for this library (human friendly).
        Type `str`. """
        
        self.topic: list[codeableconcept.CodeableConcept] | None = None
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ logic-library | model-definition | asset-collection | module-
        definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url: str | None = None
        """ Canonical identifier for this library, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.usage: str | None = None
        """ Describes the clinical usage of the library.
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the library.
        Type `str`. """
        
        super(Library, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Library, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", attachment.Attachment, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import contactdetail
from . import datarequirement
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import parameterdefinition
from . import period
from . import relatedartifact
from . import usagecontext
