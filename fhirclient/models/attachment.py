# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Attachment).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_type = "Attachment"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType: str | None = None
        """ Mime type of the content, with charset etc..
        Type `str`. """
        
        self.creation: fhirdatetime.FHIRDateTime | None = None
        """ Date attachment was first created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.data: str | None = None
        """ Data inline, base64ed.
        Type `str`. """
        
        self.hash: str | None = None
        """ Hash of the data (sha-1, base64ed).
        Type `str`. """
        
        self.language: str | None = None
        """ Human language of the content (BCP-47).
        Type `str`. """
        
        self.size: int | None = None
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self.title: str | None = None
        """ Label to display in place of the data.
        Type `str`. """
        
        self.url: str | None = None
        """ Uri where the data can be found.
        Type `str`. """
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("creation", "creation", fhirdatetime.FHIRDateTime, False, None, False),
            ("data", "data", str, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("size", "size", int, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


from . import fhirdatetime
