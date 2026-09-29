# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Location).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    
    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """
    
    resource_type = "Location"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address: address.Address | None = None
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
        
        self.alias: list[str | None] | None = None
        """ A list of alternate names that the location is known as, or was
        known as, in the past.
        List of `str` items. """
        
        self.availabilityExceptions: str | None = None
        """ Description of availability exceptions.
        Type `str`. """
        
        self.description: str | None = None
        """ Additional details about the location that could be displayed as
        further information to identify the location beyond its name.
        Type `str`. """
        
        self.endpoint: list[fhirreference.FHIRReference] | None = None
        """ Technical endpoints providing access to services operated for the
        location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.hoursOfOperation: list[LocationHoursOfOperation] | None = None
        """ What days/times during a week is this location usually open.
        List of `LocationHoursOfOperation` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization: fhirreference.FHIRReference | None = None
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.mode: str | None = None
        """ instance | kind.
        Type `str`. """
        
        self.name: str | None = None
        """ Name of the location as used by humans.
        Type `str`. """
        
        self.operationalStatus: coding.Coding | None = None
        """ The operational status of the location (typically only for a
        bed/room).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.partOf: fhirreference.FHIRReference | None = None
        """ Another Location this one is physically a part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.physicalType: codeableconcept.CodeableConcept | None = None
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.position: LocationPosition | None = None
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | suspended | inactive.
        Type `str`. """
        
        self.telecom: list[contactpoint.ContactPoint] | None = None
        """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Type of function performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("operationalStatus", "operationalStatus", coding.Coding, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("status", "status", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ What days/times during a week is this location usually open.
    """
    
    resource_type = "LocationHoursOfOperation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay: bool | None = None
        """ The Location is open all day.
        Type `bool`. """
        
        self.closingTime: fhirtime.FHIRTime | None = None
        """ Time that the Location closes.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.daysOfWeek: list[str | None] | None = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        self.openingTime: fhirtime.FHIRTime | None = None
        """ Time that the Location opens.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("closingTime", "closingTime", fhirtime.FHIRTime, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("openingTime", "openingTime", fhirtime.FHIRTime, False, None, False),
        ])
        return js


class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    
    resource_type = "LocationPosition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altitude: float | None = None
        """ Altitude with WGS84 datum.
        Type `float`. """
        
        self.latitude: float | None = None
        """ Latitude with WGS84 datum.
        Type `float`. """
        
        self.longitude: float | None = None
        """ Longitude with WGS84 datum.
        Type `float`. """
        
        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("longitude", "longitude", float, False, None, True),
        ])
        return js


from . import address
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
from . import fhirtime
from . import identifier
