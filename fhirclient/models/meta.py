# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Meta).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    
    resource_type = "Meta"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lastUpdated: fhirinstant.FHIRInstant | None = None
        """ When the resource version last changed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.profile: list[str | None] | None = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """
        
        self.security: list[coding.Coding] | None = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.source: str | None = None
        """ Identifies where the resource comes from.
        Type `str`. """
        
        self.tag: list[coding.Coding] | None = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.versionId: str | None = None
        """ Version specific identifier.
        Type `str`. """
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirinstant.FHIRInstant, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("source", "source", str, False, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js


from . import coding
from . import fhirinstant
