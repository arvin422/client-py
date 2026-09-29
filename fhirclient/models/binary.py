# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Binary).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import resource

class Binary(resource.Resource):
    """ Pure binary content defined by a format other than FHIR.
    
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    
    resource_type = "Binary"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType: str | None = None
        """ MimeType of the binary content.
        Type `str`. """
        
        self.data: str | None = None
        """ The actual content.
        Type `str`. """
        
        self.securityContext: fhirreference.FHIRReference | None = None
        """ Identifies another resource to use as proxy when enforcing access
        control.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Binary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("data", "data", str, False, None, False),
            ("securityContext", "securityContext", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import fhirreference
