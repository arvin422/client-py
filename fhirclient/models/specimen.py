# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Specimen).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Specimen(domainresource.DomainResource):
    """ Sample for analysis.
    
    A sample to be used for analysis.
    """
    
    resource_type = "Specimen"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accessionIdentifier: identifier.Identifier | None = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.collection: SpecimenCollection | None = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        
        self.condition: list[codeableconcept.CodeableConcept] | None = None
        """ State of the specimen.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.container: list[SpecimenContainer] | None = None
        """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.parent: list[fhirreference.FHIRReference] | None = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.processing: list[SpecimenProcessing] | None = None
        """ Processing and processing step details.
        List of `SpecimenProcessing` items (represented as `dict` in JSON). """
        
        self.receivedTime: fhirdatetime.FHIRDateTime | None = None
        """ The time when specimen was received for processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.request: list[fhirreference.FHIRReference] | None = None
        """ Why the specimen was collected.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Where the specimen came from. This may be from patient(s), from a
        location (e.g., the source of an environmental sample), or a
        sampling of a substance or a device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("receivedTime", "receivedTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.
    
    Details concerning the specimen collection.
    """
    
    resource_type = "SpecimenCollection"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.collectedDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Collection time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.collectedPeriod: period.Period | None = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector: fhirreference.FHIRReference | None = None
        """ Who collected the specimen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.duration: duration.Duration | None = None
        """ How long it took to collect specimen.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fastingStatusCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fastingStatusDuration: duration.Duration | None = None
        """ Whether or how long patient abstained from food and/or drink.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ The quantity of specimen collected.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("collectedDateTime", "collectedDateTime", fhirdatetime.FHIRDateTime, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("duration", "duration", duration.Duration, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", codeableconcept.CodeableConcept, False, "fastingStatus", False),
            ("fastingStatusDuration", "fastingStatusDuration", duration.Duration, False, "fastingStatus", False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).
    
    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """
    
    resource_type = "SpecimenContainer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference: fhirreference.FHIRReference | None = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.capacity: quantity.Quantity | None = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Textual description of the container.
        Type `str`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.specimenQuantity: quantity.Quantity | None = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenProcessing(backboneelement.BackboneElement):
    """ Processing and processing step details.
    
    Details concerning processing and processing steps for the specimen.
    """
    
    resource_type = "SpecimenProcessing"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive: list[fhirreference.FHIRReference] | None = None
        """ Material used in the processing step.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Textual description of procedure.
        Type `str`. """
        
        self.procedure: codeableconcept.CodeableConcept | None = None
        """ Indicates the treatment step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timeDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Date and time of specimen processing.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timePeriod: period.Period | None = None
        """ Date and time of specimen processing.
        Type `Period` (represented as `dict` in JSON). """
        
        super(SpecimenProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdatetime.FHIRDateTime, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import duration
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
