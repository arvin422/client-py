# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coding).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_type = "Coding"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ Symbol in syntax defined by the system.
        Type `str`. """
        
        self.display: str | None = None
        """ Representation defined by the system.
        Type `str`. """
        
        self.system: str | None = None
        """ Identity of the terminology system.
        Type `str`. """
        
        self.userSelected: bool | None = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """
        
        self.version: str | None = None
        """ Version of the system - if relevant.
        Type `str`. """
        
        super(Coding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


