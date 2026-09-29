# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Consent).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Consent(domainresource.DomainResource):
    """ A healthcare consumer's  choices to permit or deny recipients or roles to
    perform actions for specific purposes and periods of time.
    
    A record of a healthcare consumer’s  choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """
    
    resource_type = "Consent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: list[codeableconcept.CodeableConcept] | None = None
        """ Classification of the consent statement - for indexing/retrieval.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateTime: fhirdatetime.FHIRDateTime | None = None
        """ When this Consent was created or indexed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Identifier for this record (external references).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization: list[fhirreference.FHIRReference] | None = None
        """ Custodian of the consent.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who the consent applies to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer: list[fhirreference.FHIRReference] | None = None
        """ Who is agreeing to the policy and rules.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.policy: list[ConsentPolicy] | None = None
        """ Policies covered by this consent.
        List of `ConsentPolicy` items (represented as `dict` in JSON). """
        
        self.policyRule: codeableconcept.CodeableConcept | None = None
        """ Regulation that this consents to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provision: ConsentProvision | None = None
        """ Constraints to the base Consent.policyRule.
        Type `ConsentProvision` (represented as `dict` in JSON). """
        
        self.scope: codeableconcept.CodeableConcept | None = None
        """ Which of the four areas this resource covers (extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sourceAttachment: attachment.Attachment | None = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.sourceReference: fhirreference.FHIRReference | None = None
        """ Source from which this consent is taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """
        
        self.verification: list[ConsentVerification] | None = None
        """ Consent Verified by patient or family.
        List of `ConsentVerification` items (represented as `dict` in JSON). """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, True),
            ("dateTime", "dateTime", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("policyRule", "policyRule", codeableconcept.CodeableConcept, False, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, True),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
            ("verification", "verification", ConsentVerification, True, None, False),
        ])
        return js


from . import backboneelement

class ConsentPolicy(backboneelement.BackboneElement):
    """ Policies covered by this consent.
    
    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """
    
    resource_type = "ConsentPolicy"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority: str | None = None
        """ Enforcement source for policy.
        Type `str`. """
        
        self.uri: str | None = None
        """ Specific policy covered by this consent.
        Type `str`. """
        
        super(ConsentPolicy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


class ConsentProvision(backboneelement.BackboneElement):
    """ Constraints to the base Consent.policyRule.
    
    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """
    
    resource_type = "ConsentProvision"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[codeableconcept.CodeableConcept] | None = None
        """ Actions controlled by this rule.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor: list[ConsentProvisionActor] | None = None
        """ Who|what controlled by this rule (or group, by role).
        List of `ConsentProvisionActor` items (represented as `dict` in JSON). """
        
        self.class_fhir: list[coding.Coding] | None = None
        """ e.g. Resource Type, Profile, CDA, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.code: list[codeableconcept.CodeableConcept] | None = None
        """ e.g. LOINC or SNOMED CT code, etc. in the content.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.data: list[ConsentProvisionData] | None = None
        """ Data controlled by this rule.
        List of `ConsentProvisionData` items (represented as `dict` in JSON). """
        
        self.dataPeriod: period.Period | None = None
        """ Timeframe for data controlled by this rule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ Timeframe for this rule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provision: list[ConsentProvision] | None = None
        """ Nested Exception Rules.
        List of `ConsentProvision` items (represented as `dict` in JSON). """
        
        self.purpose: list[coding.Coding] | None = None
        """ Context of activities covered by this rule.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.securityLabel: list[coding.Coding] | None = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type: str | None = None
        """ deny | permit.
        Type `str`. """
        
        super(ConsentProvision, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ConsentProvisionActor(backboneelement.BackboneElement):
    """ Who|what controlled by this rule (or group, by role).
    
    Who or what is controlled by this rule. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """
    
    resource_type = "ConsentProvisionActor"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference: fhirreference.FHIRReference | None = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role: codeableconcept.CodeableConcept | None = None
        """ How the actor is involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConsentProvisionActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ConsentProvisionData(backboneelement.BackboneElement):
    """ Data controlled by this rule.
    
    The resources controlled by this rule if specific resources are referenced.
    """
    
    resource_type = "ConsentProvisionData"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning: str | None = None
        """ instance | related | dependents | authoredby.
        Type `str`. """
        
        self.reference: fhirreference.FHIRReference | None = None
        """ The actual data reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentProvisionData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConsentVerification(backboneelement.BackboneElement):
    """ Consent Verified by patient or family.
    
    Whether a treatment instruction (e.g. artificial respiration yes or no) was
    verified with the patient, his/her family or another authorized person.
    """
    
    resource_type = "ConsentVerification"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.verificationDate: fhirdatetime.FHIRDateTime | None = None
        """ When consent verified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.verified: bool | None = None
        """ Has been verified.
        Type `bool`. """
        
        self.verifiedWith: fhirreference.FHIRReference | None = None
        """ Person who verified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentVerification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verificationDate", "verificationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("verified", "verified", bool, False, None, True),
            ("verifiedWith", "verifiedWith", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
