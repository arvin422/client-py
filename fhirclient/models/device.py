# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Device).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    
    resource_type = "Device"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact: list[contactpoint.ContactPoint] | None = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.definition: fhirreference.FHIRReference | None = None
        """ The reference to the definition for the device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName: list[DeviceDeviceName] | None = None
        """ The name of the device as given by the manufacturer.
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """
        
        self.distinctIdentifier: str | None = None
        """ The distinct identification string.
        Type `str`. """
        
        self.expirationDate: fhirdatetime.FHIRDateTime | None = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location: fhirreference.FHIRReference | None = None
        """ Where the device is found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber: str | None = None
        """ Lot number of manufacture.
        Type `str`. """
        
        self.manufactureDate: fhirdatetime.FHIRDateTime | None = None
        """ Date when the device was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.manufacturer: str | None = None
        """ Name of device manufacturer.
        Type `str`. """
        
        self.modelNumber: str | None = None
        """ The model number for the device.
        Type `str`. """
        
        self.note: list[annotation.Annotation] | None = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.owner: fhirreference.FHIRReference | None = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parent: fhirreference.FHIRReference | None = None
        """ The parent device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partNumber: str | None = None
        """ The part number of the device.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Patient to whom Device is affixed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.property: list[DeviceProperty] | None = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceProperty` items (represented as `dict` in JSON). """
        
        self.safety: list[codeableconcept.CodeableConcept] | None = None
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serialNumber: str | None = None
        """ Serial number assigned by the manufacturer.
        Type `str`. """
        
        self.specialization: list[DeviceSpecialization] | None = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | inactive | entered-in-error | unknown.
        Type `str`. """
        
        self.statusReason: list[codeableconcept.CodeableConcept] | None = None
        """ online | paused | standby | offline | not-ready | transduc-discon |
        hw-discon | off.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ The kind or type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udiCarrier: list[DeviceUdiCarrier] | None = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """
        
        self.url: str | None = None
        """ Network address to contact device.
        Type `str`. """
        
        self.version: list[DeviceVersion] | None = None
        """ The actual design of the device or software version running on the
        device.
        List of `DeviceVersion` items (represented as `dict` in JSON). """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("expirationDate", "expirationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("status", "status", str, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.
    
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    
    resource_type = "DeviceDeviceName"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name: str | None = None
        """ The name of the device.
        Type `str`. """
        
        self.type: str | None = None
        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
        Type `str`. """
        
        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    
    resource_type = "DeviceProperty"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCode: list[codeableconcept.CodeableConcept] | None = None
        """ Property value as a code, e.g., NTP4 (synced to NTP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.valueQuantity: list[quantity.Quantity] | None = None
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js


class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    
    resource_type = "DeviceSpecialization"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType: codeableconcept.CodeableConcept | None = None
        """ The standard that is used to operate and communicate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ The version of the standard that is used to operate and communicate.
        Type `str`. """
        
        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    
    resource_type = "DeviceUdiCarrier"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC: str | None = None
        """ UDI Machine Readable Barcode String.
        Type `str`. """
        
        self.carrierHRF: str | None = None
        """ UDI Human Readable Barcode String.
        Type `str`. """
        
        self.deviceIdentifier: str | None = None
        """ Mandatory fixed portion of UDI.
        Type `str`. """
        
        self.entryType: str | None = None
        """ barcode | rfid | manual +.
        Type `str`. """
        
        self.issuer: str | None = None
        """ UDI Issuing Organization.
        Type `str`. """
        
        self.jurisdiction: str | None = None
        """ Regional UDI authority.
        Type `str`. """
        
        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
        ])
        return js


class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    
    resource_type = "DeviceVersion"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component: identifier.Identifier | None = None
        """ A single component of the device version.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ The type of the device version.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: str | None = None
        """ The version text.
        Type `str`. """
        
        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
