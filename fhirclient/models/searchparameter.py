# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SearchParameter).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base: list[str | None] | None = None
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """
        
        self.chain: list[str | None] | None = None
        """ Chained names supported.
        List of `str` items. """
        
        self.code: str | None = None
        """ Code used in URL.
        Type `str`. """
        
        self.comparator: list[str | None] | None = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """
        
        self.component: list[SearchParameterComponent] | None = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        
        self.contact: list[contactdetail.ContactDetail] | None = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.derivedFrom: str | None = None
        """ Original definition for the search parameter.
        Type `str`. """
        
        self.description: str | None = None
        """ Natural language description of the search parameter.
        Type `str`. """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.expression: str | None = None
        """ FHIRPath expression that extracts the values.
        Type `str`. """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.modifier: list[str | None] | None = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `str` items. """
        
        self.multipleAnd: bool | None = None
        """ Allow multiple parameters (and).
        Type `bool`. """
        
        self.multipleOr: bool | None = None
        """ Allow multiple values per parameter (or).
        Type `bool`. """
        
        self.name: str | None = None
        """ Name for this search parameter (computer friendly).
        Type `str`. """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose: str | None = None
        """ Why this search parameter is defined.
        Type `str`. """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.target: list[str | None] | None = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.type: str | None = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the search parameter.
        Type `str`. """
        
        self.xpath: str | None = None
        """ XPath that extracts the values.
        Type `str`. """
        
        self.xpathUsage: str | None = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, True, None, True),
            ("chain", "chain", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("comparator", "comparator", str, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("description", "description", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("target", "target", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.
    
    Used to define the parts of a composite search parameter.
    """
    
    resource_type = "SearchParameterComponent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition: str | None = None
        """ Defines how the part works.
        Type `str`. """
        
        self.expression: str | None = None
        """ Subexpression relative to main expression.
        Type `str`. """
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("expression", "expression", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import usagecontext
