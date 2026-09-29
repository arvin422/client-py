# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HealthcareService).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_type = "HealthcareService"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active: bool | None = None
        """ Whether this HealthcareService record is in active use.
        Type `bool`. """
        
        self.appointmentRequired: bool | None = None
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self.availabilityExceptions: str | None = None
        """ Description of availability exceptions.
        Type `str`. """
        
        self.availableTime: list[HealthcareServiceAvailableTime] | None = None
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Broad category of service being performed or delivered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.characteristic: list[codeableconcept.CodeableConcept] | None = None
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment: str | None = None
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
        
        self.communication: list[codeableconcept.CodeableConcept] | None = None
        """ The language that this service is offered in.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.coverageArea: list[fhirreference.FHIRReference] | None = None
        """ Location(s) service is intended for/available to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.eligibility: list[HealthcareServiceEligibility] | None = None
        """ Specific eligibility requirements required to use the service.
        List of `HealthcareServiceEligibility` items (represented as `dict` in JSON). """
        
        self.endpoint: list[fhirreference.FHIRReference] | None = None
        """ Technical endpoints providing access to electronic services
        operated for the healthcare service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.extraDetails: str | None = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location: list[fhirreference.FHIRReference] | None = None
        """ Location(s) where service may be provided.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        
        self.notAvailable: list[HealthcareServiceNotAvailable] | None = None
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo: attachment.Attachment | None = None
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.program: list[codeableconcept.CodeableConcept] | None = None
        """ Programs that this service is applicable to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.providedBy: fhirreference.FHIRReference | None = None
        """ Organization that provides this service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referralMethod: list[codeableconcept.CodeableConcept] | None = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceProvisionCode: list[codeableconcept.CodeableConcept] | None = None
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty: list[codeableconcept.CodeableConcept] | None = None
        """ Specialties handled by the HealthcareService.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom: list[contactpoint.ContactPoint] | None = None
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Type of service that may be delivered or performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("program", "program", codeableconcept.CodeableConcept, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_type = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay: bool | None = None
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        
        self.availableEndTime: fhirtime.FHIRTime | None = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.availableStartTime: fhirtime.FHIRTime | None = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.daysOfWeek: list[str | None] | None = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirtime.FHIRTime, False, None, False),
            ("availableStartTime", "availableStartTime", fhirtime.FHIRTime, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.
    
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    
    resource_type = "HealthcareServiceEligibility"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Coded value for the eligibility.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment: str | None = None
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        
        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_type = "HealthcareServiceNotAvailable"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self.during: period.Period | None = None
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period
