# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageHeader).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_type = "MessageHeader"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author: fhirreference.FHIRReference | None = None
        """ The source of the decision.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definition: str | None = None
        """ Link to the definition for this message.
        Type `str`. """
        
        self.destination: list[MessageHeaderDestination] | None = None
        """ Message destination application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        
        self.enterer: fhirreference.FHIRReference | None = None
        """ The source of the data entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.eventCoding: coding.Coding | None = None
        """ Code for the event this message represents or link to event
        definition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri: str | None = None
        """ Code for the event this message represents or link to event
        definition.
        Type `str`. """
        
        self.focus: list[fhirreference.FHIRReference] | None = None
        """ The actual content of the message.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reason: codeableconcept.CodeableConcept | None = None
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.response: MessageHeaderResponse | None = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.responsible: fhirreference.FHIRReference | None = None
        """ Final responsibility for event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sender: fhirreference.FHIRReference | None = None
        """ Real world sender of the message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source: MessageHeaderSource | None = None
        """ Message source application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
        ])
        return js


from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).
    
    The destination application which the message is intended for.
    """
    
    resource_type = "MessageHeaderDestination"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint: str | None = None
        """ Actual destination address or id.
        Type `str`. """
        
        self.name: str | None = None
        """ Name of system.
        Type `str`. """
        
        self.receiver: fhirreference.FHIRReference | None = None
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.target: fhirreference.FHIRReference | None = None
        """ Particular delivery destination within the destination.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    resource_type = "MessageHeaderResponse"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: str | None = None
        """ ok | transient-error | fatal-error.
        Type `str`. """
        
        self.details: fhirreference.FHIRReference | None = None
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: str | None = None
        """ Id of original message.
        Type `str`. """
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", str, False, None, True),
        ])
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.
    
    The source application from which this message originated.
    """
    
    resource_type = "MessageHeaderSource"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact: contactpoint.ContactPoint | None = None
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.endpoint: str | None = None
        """ Actual message source address or id.
        Type `str`. """
        
        self.name: str | None = None
        """ Name of system.
        Type `str`. """
        
        self.software: str | None = None
        """ Name of software running the system.
        Type `str`. """
        
        self.version: str | None = None
        """ Version of software running.
        Type `str`. """
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("software", "software", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference
