# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Endpoint).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Endpoint(domainresource.DomainResource):
    """ The technical details of an endpoint that can be used for electronic
    services.
    
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b or a REST endpoint for
    another FHIR server. This may include any security context information.
    """
    
    resource_type = "Endpoint"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address: str | None = None
        """ The technical base address for connecting to this endpoint.
        Type `str`. """
        
        self.connectionType: coding.Coding | None = None
        """ Protocol/Profile/Standard to be used with this endpoint connection.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.contact: list[contactpoint.ContactPoint] | None = None
        """ Contact details for source (e.g. troubleshooting).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.header: list[str | None] | None = None
        """ Usage depends on the channel type.
        List of `str` items. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Identifies this endpoint across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization: fhirreference.FHIRReference | None = None
        """ Organization that manages this endpoint (might not be the
        organization that exposes the endpoint).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ A name that this endpoint can be identified by.
        Type `str`. """
        
        self.payloadMimeType: list[str | None] | None = None
        """ Mimetype to send. If not specified, the content could be anything
        (including no payload, if the connectionType defined this).
        List of `str` items. """
        
        self.payloadType: list[codeableconcept.CodeableConcept] | None = None
        """ The type of content that may be used at this endpoint (e.g. XDS
        Discharge summaries).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ Interval the endpoint is expected to be operational.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | suspended | error | off | entered-in-error | test.
        Type `str`. """
        
        super(Endpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Endpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("connectionType", "connectionType", coding.Coding, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("header", "header", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("payloadMimeType", "payloadMimeType", str, True, None, False),
            ("payloadType", "payloadType", codeableconcept.CodeableConcept, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import identifier
from . import period
