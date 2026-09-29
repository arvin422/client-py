# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.
    
    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    
    resource_type = "CoverageEligibilityRequest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.enterer: fhirreference.FHIRReference | None = None
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility: fhirreference.FHIRReference | None = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance: list[CoverageEligibilityRequestInsurance] | None = None
        """ Patient insurance information.
        List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON). """
        
        self.insurer: fhirreference.FHIRReference | None = None
        """ Coverage issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item: list[CoverageEligibilityRequestItem] | None = None
        """ Item to be evaluated for eligibiity.
        List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Intended recipient of products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority: codeableconcept.CodeableConcept | None = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Party responsible for the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.purpose: list[str | None] | None = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        
        self.servicedDate: fhirdate.FHIRDate | None = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod: period.Period | None = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.supportingInfo: list[CoverageEligibilityRequestSupportingInfo] | None = None
        """ Supporting information.
        List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services.
    """
    
    resource_type = "CoverageEligibilityRequestInsurance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement: str | None = None
        """ Additional provider contract number.
        Type `str`. """
        
        self.coverage: fhirreference.FHIRReference | None = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal: bool | None = None
        """ Applicable coverage.
        Type `bool`. """
        
        super(CoverageEligibilityRequestInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Item to be evaluated for eligibiity.
    
    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    
    resource_type = "CoverageEligibilityRequestItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail: list[fhirreference.FHIRReference] | None = None
        """ Product or service details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.diagnosis: list[CoverageEligibilityRequestItemDiagnosis] | None = None
        """ Applicable diagnosis.
        List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON). """
        
        self.facility: fhirreference.FHIRReference | None = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Perfoming practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.supportingInfoSequence: list[int | None] | None = None
        """ Applicable exception or supporting information.
        List of `int` items. """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ Applicable diagnosis.
    
    Patient diagnosis for which care is sought.
    """
    
    resource_type = "CoverageEligibilityRequestItemDiagnosis"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Nature of illness or problem.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference: fhirreference.FHIRReference | None = None
        """ Nature of illness or problem.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItemDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
        ])
        return js


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "CoverageEligibilityRequestSupportingInfo"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appliesToAll: bool | None = None
        """ Applies to all items.
        Type `bool`. """
        
        self.information: fhirreference.FHIRReference | None = None
        """ Data to be provided.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Information instance identifier.
        Type `int`. """
        
        super(CoverageEligibilityRequestSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("information", "information", fhirreference.FHIRReference, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
