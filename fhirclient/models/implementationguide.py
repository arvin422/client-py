# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImplementationGuide).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.
    
    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """
    
    resource_type = "ImplementationGuide"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact: list[contactdetail.ContactDetail] | None = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright: str | None = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.definition: ImplementationGuideDefinition | None = None
        """ Information needed to build the IG.
        Type `ImplementationGuideDefinition` (represented as `dict` in JSON). """
        
        self.dependsOn: list[ImplementationGuideDependsOn] | None = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependsOn` items (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Natural language description of the implementation guide.
        Type `str`. """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion: list[str | None] | None = None
        """ FHIR Version(s) this Implementation Guide targets.
        List of `str` items. """
        
        self.global_fhir: list[ImplementationGuideGlobal] | None = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for implementation guide (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.license: str | None = None
        """ SPDX license code for this IG (or not-open-source).
        Type `str`. """
        
        self.manifest: ImplementationGuideManifest | None = None
        """ Information about an assembled IG.
        Type `ImplementationGuideManifest` (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Name for this implementation guide (computer friendly).
        Type `str`. """
        
        self.packageId: str | None = None
        """ NPM Package name for IG.
        Type `str`. """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.title: str | None = None
        """ Name for this implementation guide (human friendly).
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical identifier for this implementation guide, represented as
        a URI (globally unique).
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the implementation guide.
        Type `str`. """
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("definition", "definition", ImplementationGuideDefinition, False, None, False),
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, True),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("license", "license", str, False, None, False),
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False),
            ("name", "name", str, False, None, True),
            ("packageId", "packageId", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.
    
    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """
    
    resource_type = "ImplementationGuideDefinition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.grouping: list[ImplementationGuideDefinitionGrouping] | None = None
        """ Grouping used to present related resources in the IG.
        List of `ImplementationGuideDefinitionGrouping` items (represented as `dict` in JSON). """
        
        self.page: ImplementationGuideDefinitionPage | None = None
        """ Page/Section in the Guide.
        Type `ImplementationGuideDefinitionPage` (represented as `dict` in JSON). """
        
        self.parameter: list[ImplementationGuideDefinitionParameter] | None = None
        """ Defines how IG is built by tools.
        List of `ImplementationGuideDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.resource: list[ImplementationGuideDefinitionResource] | None = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideDefinitionResource` items (represented as `dict` in JSON). """
        
        self.template: list[ImplementationGuideDefinitionTemplate] | None = None
        """ A template for building resources.
        List of `ImplementationGuideDefinitionTemplate` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False),
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False),
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False),
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True),
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False),
        ])
        return js


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.
    
    A logical group of resources. Logical groups can be used when building
    pages.
    """
    
    resource_type = "ImplementationGuideDefinitionGrouping"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Human readable text describing the package.
        Type `str`. """
        
        self.name: str | None = None
        """ Descriptive name for the package.
        Type `str`. """
        
        super(ImplementationGuideDefinitionGrouping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.
    
    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """
    
    resource_type = "ImplementationGuideDefinitionPage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.generation: str | None = None
        """ html | markdown | xml | generated.
        Type `str`. """
        
        self.nameReference: fhirreference.FHIRReference | None = None
        """ Where to find that page.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.nameUrl: str | None = None
        """ Where to find that page.
        Type `str`. """
        
        self.page: list[ImplementationGuideDefinitionPage] | None = None
        """ Nested Pages / Sections.
        List of `ImplementationGuideDefinitionPage` items (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Short title shown for navigational assistance.
        Type `str`. """
        
        super(ImplementationGuideDefinitionPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("generation", "generation", str, False, None, True),
            ("nameReference", "nameReference", fhirreference.FHIRReference, False, "name", True),
            ("nameUrl", "nameUrl", str, False, "name", True),
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """
    
    resource_type = "ImplementationGuideDefinitionParameter"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ apply | path-resource | path-pages | path-tx-cache | expansion-
        parameter | rule-broken-links | generate-xml | generate-json |
        generate-turtle | html-template.
        Type `str`. """
        
        self.value: str | None = None
        """ Value for named type.
        Type `str`. """
        
        super(ImplementationGuideDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_type = "ImplementationGuideDefinitionResource"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Reason why included in guide.
        Type `str`. """
        
        self.exampleBoolean: bool | None = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        
        self.exampleCanonical: str | None = None
        """ Is an example/What is this an example of?.
        Type `str`. """
        
        self.fhirVersion: list[str | None] | None = None
        """ Versions this applies to (if different to IG).
        List of `str` items. """
        
        self.groupingId: str | None = None
        """ Grouping this is part of.
        Type `str`. """
        
        self.name: str | None = None
        """ Human Name for the resource.
        Type `str`. """
        
        self.reference: fhirreference.FHIRReference | None = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("fhirVersion", "fhirVersion", str, True, None, False),
            ("groupingId", "groupingId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """
    
    resource_type = "ImplementationGuideDefinitionTemplate"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ Type of template specified.
        Type `str`. """
        
        self.scope: str | None = None
        """ The scope in which the template applies.
        Type `str`. """
        
        self.source: str | None = None
        """ The source location for the template.
        Type `str`. """
        
        super(ImplementationGuideDefinitionTemplate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("scope", "scope", str, False, None, False),
            ("source", "source", str, False, None, True),
        ])
        return js


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.
    
    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """
    
    resource_type = "ImplementationGuideDependsOn"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.packageId: str | None = None
        """ NPM Package name for IG this depends on.
        Type `str`. """
        
        self.uri: str | None = None
        """ Identity of the IG that this depends on.
        Type `str`. """
        
        self.version: str | None = None
        """ Version of the IG.
        Type `str`. """
        
        super(ImplementationGuideDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("packageId", "packageId", str, False, None, False),
            ("uri", "uri", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.
    
    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """
    
    resource_type = "ImplementationGuideGlobal"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.profile: str | None = None
        """ Profile that all resources must conform to.
        Type `str`. """
        
        self.type: str | None = None
        """ Type this profile applies to.
        Type `str`. """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.
    
    Information about an assembled implementation guide, created by the
    publication tooling.
    """
    
    resource_type = "ImplementationGuideManifest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.image: list[str | None] | None = None
        """ Image within the IG.
        List of `str` items. """
        
        self.other: list[str | None] | None = None
        """ Additional linkable file in IG.
        List of `str` items. """
        
        self.page: list[ImplementationGuideManifestPage] | None = None
        """ HTML page within the parent IG.
        List of `ImplementationGuideManifestPage` items (represented as `dict` in JSON). """
        
        self.rendering: str | None = None
        """ Location of rendered implementation guide.
        Type `str`. """
        
        self.resource: list[ImplementationGuideManifestResource] | None = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideManifestResource` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("image", "image", str, True, None, False),
            ("other", "other", str, True, None, False),
            ("page", "page", ImplementationGuideManifestPage, True, None, False),
            ("rendering", "rendering", str, False, None, False),
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True),
        ])
        return js


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.
    
    Information about a page within the IG.
    """
    
    resource_type = "ImplementationGuideManifestPage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.anchor: list[str | None] | None = None
        """ Anchor available on the page.
        List of `str` items. """
        
        self.name: str | None = None
        """ HTML page name.
        Type `str`. """
        
        self.title: str | None = None
        """ Title of the page, for references.
        Type `str`. """
        
        super(ImplementationGuideManifestPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("anchor", "anchor", str, True, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
        ])
        return js


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.
    
    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """
    
    resource_type = "ImplementationGuideManifestResource"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exampleBoolean: bool | None = None
        """ Is an example/What is this an example of?.
        Type `bool`. """
        
        self.exampleCanonical: str | None = None
        """ Is an example/What is this an example of?.
        Type `str`. """
        
        self.reference: fhirreference.FHIRReference | None = None
        """ Location of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relativePath: str | None = None
        """ Relative path for page in IG.
        Type `str`. """
        
        super(ImplementationGuideManifestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("relativePath", "relativePath", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdatetime
from . import fhirreference
from . import usagecontext
