# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_type = "AppointmentResponse"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor: fhirreference.FHIRReference | None = None
        """ Person, Location, HealthcareService, or Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.appointment: fhirreference.FHIRReference | None = None
        """ Appointment this response relates to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.comment: str | None = None
        """ Additional comments.
        Type `str`. """
        
        self.end: fhirinstant.FHIRInstant | None = None
        """ Time from appointment, or requested new end time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.participantStatus: str | None = None
        """ accepted | declined | tentative | needs-action.
        Type `str`. """
        
        self.participantType: list[codeableconcept.CodeableConcept] | None = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start: fhirinstant.FHIRInstant | None = None
        """ Time from appointment, or requested new start time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("end", "end", fhirinstant.FHIRInstant, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirinstant.FHIRInstant, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirinstant
from . import fhirreference
from . import identifier
