# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enroll in coverage.
    
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    
    resource_type = "EnrollmentRequest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.candidate: fhirreference.FHIRReference | None = None
        """ The subject to be enrolled.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage: fhirreference.FHIRReference | None = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurer: fhirreference.FHIRReference | None = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import fhirdatetime
from . import fhirreference
from . import identifier
