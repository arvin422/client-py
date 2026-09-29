# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Communication).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """
    
    resource_type = "Communication"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.about: list[fhirreference.FHIRReference] | None = None
        """ Resources that pertain to this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ Request fulfilled by this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.inResponseTo: list[fhirreference.FHIRReference] | None = None
        """ Reply to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: list[str | None] | None = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        
        self.instantiatesUri: list[str | None] | None = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        
        self.medium: list[codeableconcept.CodeableConcept] | None = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments made about the communication.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf: list[fhirreference.FHIRReference] | None = None
        """ Part of this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.payload: list[CommunicationPayload] | None = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        
        self.priority: str | None = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why was communication done?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.received: fhirdatetime.FHIRDateTime | None = None
        """ When received.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recipient: list[fhirreference.FHIRReference] | None = None
        """ Message recipient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sender: fhirreference.FHIRReference | None = None
        """ Message sender.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sent: fhirdatetime.FHIRDateTime | None = None
        """ When sent.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.status: str | None = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        
        self.statusReason: codeableconcept.CodeableConcept | None = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Focus of message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.topic: codeableconcept.CodeableConcept | None = None
        """ Description of the purpose/content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Communication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Communication, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("inResponseTo", "inResponseTo", fhirreference.FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("received", "received", fhirdatetime.FHIRDateTime, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("sent", "sent", fhirdatetime.FHIRDateTime, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    
    resource_type = "CommunicationPayload"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment: attachment.Attachment | None = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference: fhirreference.FHIRReference | None = None
        """ Message part content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contentString: str | None = None
        """ Message part content.
        Type `str`. """
        
        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


from . import annotation
from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
