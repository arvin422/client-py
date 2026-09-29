# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Contract).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Contract(domainresource.DomainResource):
    """ Legal Agreement.
    
    Legally enforceable, formally recorded unilateral or bilateral directive
    i.e., a policy or agreement.
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias: list[str | None] | None = None
        """ Acronym or short name.
        List of `str` items. """
        
        self.applies: period.Period | None = None
        """ Effective time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.author: fhirreference.FHIRReference | None = None
        """ Source of Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authority: list[fhirreference.FHIRReference] | None = None
        """ Authority under which this Contract has standing.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.contentDefinition: ContractContentDefinition | None = None
        """ Contract precursor content.
        Type `ContractContentDefinition` (represented as `dict` in JSON). """
        
        self.contentDerivative: codeableconcept.CodeableConcept | None = None
        """ Content derived from the basal information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain: list[fhirreference.FHIRReference] | None = None
        """ A sphere of control governed by an authoritative jurisdiction,
        organization, or person.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.expirationType: codeableconcept.CodeableConcept | None = None
        """ Contract cessation cause.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.friendly: list[ContractFriendly] | None = None
        """ Contract Friendly Language.
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Contract number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: fhirreference.FHIRReference | None = None
        """ Source Contract Definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.instantiatesUri: str | None = None
        """ External Contract Definition.
        Type `str`. """
        
        self.issued: fhirdatetime.FHIRDateTime | None = None
        """ When this Contract was issued.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.legal: list[ContractLegal] | None = None
        """ Contract Legal Language.
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.legalState: codeableconcept.CodeableConcept | None = None
        """ Negotiation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.legallyBindingAttachment: attachment.Attachment | None = None
        """ Binding Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.legallyBindingReference: fhirreference.FHIRReference | None = None
        """ Binding Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Computer friendly designation.
        Type `str`. """
        
        self.relevantHistory: list[fhirreference.FHIRReference] | None = None
        """ Key event in Contract History.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.rule: list[ContractRule] | None = None
        """ Computable Contract Language.
        List of `ContractRule` items (represented as `dict` in JSON). """
        
        self.scope: codeableconcept.CodeableConcept | None = None
        """ Range of Legal Concerns.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.signer: list[ContractSigner] | None = None
        """ Contract Signatory.
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.site: list[fhirreference.FHIRReference] | None = None
        """ Specific Location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        
        self.subType: list[codeableconcept.CodeableConcept] | None = None
        """ Subtype within the context of type.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject: list[fhirreference.FHIRReference] | None = None
        """ Contract Target Entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subtitle: str | None = None
        """ Subordinate Friendly name.
        Type `str`. """
        
        self.supportingInfo: list[fhirreference.FHIRReference] | None = None
        """ Extra Information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.term: list[ContractTerm] | None = None
        """ Contract Term List.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Human Friendly name.
        Type `str`. """
        
        self.topicCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Focus of contract interest.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference: fhirreference.FHIRReference | None = None
        """ Focus of contract interest.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Legal instrument category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url: str | None = None
        """ Basal definition.
        Type `str`. """
        
        self.version: str | None = None
        """ Business edition.
        Type `str`. """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("name", "name", str, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("title", "title", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ContractContentDefinition(backboneelement.BackboneElement):
    """ Contract precursor content.
    
    Precusory content developed with a focus and intent of supporting the
    formation a Contract instance, which may be associated with and
    transformable into a Contract.
    """
    
    resource_type = "ContractContentDefinition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.copyright: str | None = None
        """ Publication Ownership.
        Type `str`. """
        
        self.publicationDate: fhirdatetime.FHIRDateTime | None = None
        """ When published.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publicationStatus: str | None = None
        """ amended | appended | cancelled | disputed | entered-in-error |
        executable | executed | negotiable | offered | policy | rejected |
        renewed | revoked | resolved | terminated.
        Type `str`. """
        
        self.publisher: fhirreference.FHIRReference | None = None
        """ Publisher Entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subType: codeableconcept.CodeableConcept | None = None
        """ Detailed Content Type Definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Content structure and use.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractContentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractFriendly(backboneelement.BackboneElement):
    """ Contract Friendly Language.
    
    The "patient friendly language" versionof the Contract in whole or in
    parts. "Patient friendly language" means the representation of the Contract
    and Contract Provisions in a manner that is readily accessible and
    understandable by a layperson in accordance with best practices for
    communication styles that ensure that those agreeing to or signing the
    Contract understand the roles, actions, obligations, responsibilities, and
    implication of the agreement.
    """
    
    resource_type = "ContractFriendly"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment: attachment.Attachment | None = None
        """ Easily comprehended representation of this Contract.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference: fhirreference.FHIRReference | None = None
        """ Easily comprehended representation of this Contract.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractLegal(backboneelement.BackboneElement):
    """ Contract Legal Language.
    
    List of Legal expressions or representations of this Contract.
    """
    
    resource_type = "ContractLegal"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment: attachment.Attachment | None = None
        """ Contract Legal Text.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference: fhirreference.FHIRReference | None = None
        """ Contract Legal Text.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractRule(backboneelement.BackboneElement):
    """ Computable Contract Language.
    
    List of Computable Policy Rule Language Representations of this Contract.
    """
    
    resource_type = "ContractRule"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment: attachment.Attachment | None = None
        """ Computable Contract Rules.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference: fhirreference.FHIRReference | None = None
        """ Computable Contract Rules.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractSigner(backboneelement.BackboneElement):
    """ Contract Signatory.
    
    Parties with legal standing in the Contract, including the principal
    parties, the grantor(s) and grantee(s), which are any person or
    organization bound by the contract, and any ancillary parties, which
    facilitate the execution of the contract such as a notary or witness.
    """
    
    resource_type = "ContractSigner"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party: fhirreference.FHIRReference | None = None
        """ Contract Signatory Party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.signature: list[signature.Signature] | None = None
        """ Contract Documentation Signature.
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.type: coding.Coding | None = None
        """ Contract Signatory Role.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", signature.Signature, True, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ContractTerm(backboneelement.BackboneElement):
    """ Contract Term List.
    
    One or more Contract Provisions, which may be related and conveyed as a
    group, and may contain nested groups.
    """
    
    resource_type = "ContractTerm"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[ContractTermAction] | None = None
        """ Entity being ascribed responsibility.
        List of `ContractTermAction` items (represented as `dict` in JSON). """
        
        self.applies: period.Period | None = None
        """ Contract Term Effective Time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.asset: list[ContractTermAsset] | None = None
        """ Contract Term Asset List.
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        
        self.group: list[ContractTerm] | None = None
        """ Nested Contract Term Group.
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Contract Term Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued: fhirdatetime.FHIRDateTime | None = None
        """ Contract Term Issue Date Time.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.offer: ContractTermOffer | None = None
        """ Context of the Contract term.
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        
        self.securityLabel: list[ContractTermSecurityLabel] | None = None
        """ Protection for the Term.
        List of `ContractTermSecurityLabel` items (represented as `dict` in JSON). """
        
        self.subType: codeableconcept.CodeableConcept | None = None
        """ Contract Term Type specific classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Term Statement.
        Type `str`. """
        
        self.topicCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Term Concern.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference: fhirreference.FHIRReference | None = None
        """ Term Concern.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Contract Term Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAction(backboneelement.BackboneElement):
    """ Entity being ascribed responsibility.
    
    An actor taking a role in an activity for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    resource_type = "ContractTermAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context: fhirreference.FHIRReference | None = None
        """ Episode associated with action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contextLinkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.doNotPerform: bool | None = None
        """ True if the term prohibits the  action.
        Type `bool`. """
        
        self.intent: codeableconcept.CodeableConcept | None = None
        """ Purpose for the Contract Term Action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.linkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments about the action.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime: fhirdatetime.FHIRDateTime | None = None
        """ When action happens.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod: period.Period | None = None
        """ When action happens.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming: timing.Timing | None = None
        """ When action happens.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.performer: fhirreference.FHIRReference | None = None
        """ Actor that wil execute (or not) the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerLinkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.performerRole: codeableconcept.CodeableConcept | None = None
        """ Competency of the performer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performerType: list[codeableconcept.CodeableConcept] | None = None
        """ Kind of service performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reason: list[str | None] | None = None
        """ Why action is to be performed.
        List of `str` items. """
        
        self.reasonCode: list[codeableconcept.CodeableConcept] | None = None
        """ Why is action (not) needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonLinkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.reasonReference: list[fhirreference.FHIRReference] | None = None
        """ Why is action (not) needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester: list[fhirreference.FHIRReference] | None = None
        """ Who asked for action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requesterLinkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.securityLabelNumber: list[int | None] | None = None
        """ Action restriction numbers.
        List of `int` items. """
        
        self.status: codeableconcept.CodeableConcept | None = None
        """ State of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject: list[ContractTermActionSubject] | None = None
        """ Entity of the action.
        List of `ContractTermActionSubject` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type or form of the action.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True),
            ("linkId", "linkId", str, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("reason", "reason", str, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, True, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermActionSubject(backboneelement.BackboneElement):
    """ Entity of the action.
    """
    
    resource_type = "ContractTermActionSubject"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference: list[fhirreference.FHIRReference] | None = None
        """ Entity of the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role: codeableconcept.CodeableConcept | None = None
        """ Role type of the agent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermActionSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAsset(backboneelement.BackboneElement):
    """ Contract Term Asset List.
    """
    
    resource_type = "ContractTermAsset"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer: list[ContractTermOfferAnswer] | None = None
        """ Response to assets.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.condition: str | None = None
        """ Quality desctiption of asset.
        Type `str`. """
        
        self.context: list[ContractTermAssetContext] | None = None
        """ Circumstance of the asset.
        List of `ContractTermAssetContext` items (represented as `dict` in JSON). """
        
        self.linkId: list[str | None] | None = None
        """ Pointer to asset text.
        List of `str` items. """
        
        self.period: list[period.Period] | None = None
        """ Time period of the asset.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.periodType: list[codeableconcept.CodeableConcept] | None = None
        """ Asset availability types.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relationship: coding.Coding | None = None
        """ Kinship of the asset.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.scope: codeableconcept.CodeableConcept | None = None
        """ Range of asset.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.securityLabelNumber: list[int | None] | None = None
        """ Asset restriction numbers.
        List of `int` items. """
        
        self.subtype: list[codeableconcept.CodeableConcept] | None = None
        """ Asset sub-category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Asset clause or question text.
        Type `str`. """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Asset category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.typeReference: list[fhirreference.FHIRReference] | None = None
        """ Associated entities.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usePeriod: list[period.Period] | None = None
        """ Time period.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.valuedItem: list[ContractTermAssetValuedItem] | None = None
        """ Contract Valued Item List.
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("period", "period", period.Period, True, None, False),
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False),
            ("usePeriod", "usePeriod", period.Period, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js


class ContractTermAssetContext(backboneelement.BackboneElement):
    """ Circumstance of the asset.
    """
    
    resource_type = "ContractTermAssetContext"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: list[codeableconcept.CodeableConcept] | None = None
        """ Codeable asset context.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reference: fhirreference.FHIRReference | None = None
        """ Creator,custodian or owner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.text: str | None = None
        """ Context description.
        Type `str`. """
        
        super(ContractTermAssetContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ Contract Valued Item List.
    """
    
    resource_type = "ContractTermAssetValuedItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effectiveTime: fhirdatetime.FHIRDateTime | None = None
        """ Contract Valued Item Effective Tiem.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.entityCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Contract Valued Item Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference: fhirreference.FHIRReference | None = None
        """ Contract Valued Item Type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Contract Valued Item Price Scaling Factor.
        Type `float`. """
        
        self.identifier: identifier.Identifier | None = None
        """ Contract Valued Item Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.linkId: list[str | None] | None = None
        """ Pointer to specific item.
        List of `str` items. """
        
        self.net: money.Money | None = None
        """ Total Contract Valued Item Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.payment: str | None = None
        """ Terms of valuation.
        Type `str`. """
        
        self.paymentDate: fhirdatetime.FHIRDateTime | None = None
        """ When payment is due.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.points: float | None = None
        """ Contract Valued Item Difficulty Scaling Factor.
        Type `float`. """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of Contract Valued Items.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.recipient: fhirreference.FHIRReference | None = None
        """ Who will receive payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible: fhirreference.FHIRReference | None = None
        """ Who will make payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.securityLabelNumber: list[int | None] | None = None
        """ Security Labels that define affected terms.
        List of `int` items. """
        
        self.unitPrice: money.Money | None = None
        """ Contract Valued Item fee, charge, or cost.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("paymentDate", "paymentDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ContractTermOffer(backboneelement.BackboneElement):
    """ Context of the Contract term.
    
    The matter of concern in the context of this provision of the agrement.
    """
    
    resource_type = "ContractTermOffer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer: list[ContractTermOfferAnswer] | None = None
        """ Response to offer text.
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.decision: codeableconcept.CodeableConcept | None = None
        """ Accepting party choice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decisionMode: list[codeableconcept.CodeableConcept] | None = None
        """ How decision is conveyed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Offer business ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.linkId: list[str | None] | None = None
        """ Pointer to text.
        List of `str` items. """
        
        self.party: list[ContractTermOfferParty] | None = None
        """ Offer Recipient.
        List of `ContractTermOfferParty` items (represented as `dict` in JSON). """
        
        self.securityLabelNumber: list[int | None] | None = None
        """ Offer restriction numbers.
        List of `int` items. """
        
        self.text: str | None = None
        """ Human readable offer text.
        Type `str`. """
        
        self.topic: fhirreference.FHIRReference | None = None
        """ Negotiable offer asset.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Contract Offer Type or Form.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ Response to offer text.
    """
    
    resource_type = "ContractTermOfferAnswer"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ The actual answer response.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ The actual answer response.
        Type `bool`. """
        
        self.valueCoding: coding.Coding | None = None
        """ The actual answer response.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ The actual answer response.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ The actual answer response.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal: float | None = None
        """ The actual answer response.
        Type `float`. """
        
        self.valueInteger: int | None = None
        """ The actual answer response.
        Type `int`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ The actual answer response.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ The actual answer response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ The actual answer response.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ The actual answer response.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUri: str | None = None
        """ The actual answer response.
        Type `str`. """
        
        super(ContractTermOfferAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermOfferAnswer, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


class ContractTermOfferParty(backboneelement.BackboneElement):
    """ Offer Recipient.
    """
    
    resource_type = "ContractTermOfferParty"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference: list[fhirreference.FHIRReference] | None = None
        """ Referenced entity.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role: codeableconcept.CodeableConcept | None = None
        """ Participant engagement type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOfferParty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ Protection for the Term.
    
    Security labels that protect the handling of information about the term and
    its elements, which may be specifically identified..
    """
    
    resource_type = "ContractTermSecurityLabel"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: list[coding.Coding] | None = None
        """ Applicable Policy.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.classification: coding.Coding | None = None
        """ Confidentiality Protection.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.control: list[coding.Coding] | None = None
        """ Handling Instructions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.number: list[int | None] | None = None
        """ Link to Security Labels.
        List of `int` items. """
        
        super(ContractTermSecurityLabel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, True, None, False),
            ("classification", "classification", coding.Coding, False, None, True),
            ("control", "control", coding.Coding, True, None, False),
            ("number", "number", int, True, None, False),
        ])
        return js


from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import fhirtime
from . import identifier
from . import money
from . import period
from . import quantity
from . import signature
from . import timing
