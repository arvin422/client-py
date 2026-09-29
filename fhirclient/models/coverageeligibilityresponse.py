# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class CoverageEligibilityResponse(domainresource.DomainResource):
    """ CoverageEligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    
    resource_type = "CoverageEligibilityResponse"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.disposition: str | None = None
        """ Disposition Message.
        Type `str`. """
        
        self.error: list[CoverageEligibilityResponseError] | None = None
        """ Processing errors.
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """
        
        self.form: codeableconcept.CodeableConcept | None = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance: list[CoverageEligibilityResponseInsurance] | None = None
        """ Patient insurance information.
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer: fhirreference.FHIRReference | None = None
        """ Coverage issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome: str | None = None
        """ queued | complete | error | partial.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Intended recipient of products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.preAuthRef: str | None = None
        """ Preauthorization reference.
        Type `str`. """
        
        self.purpose: list[str | None] | None = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        
        self.request: fhirreference.FHIRReference | None = None
        """ Eligibility request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor: fhirreference.FHIRReference | None = None
        """ Party responsible for the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicedDate: fhirdate.FHIRDate | None = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod: period.Period | None = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(CoverageEligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Errors encountered during the processing of the request.
    """
    
    resource_type = "CoverageEligibilityResponseError"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services.
    """
    
    resource_type = "CoverageEligibilityResponseInsurance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitPeriod: period.Period | None = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """
        
        self.coverage: fhirreference.FHIRReference | None = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.inforce: bool | None = None
        """ Coverage inforce indicator.
        Type `bool`. """
        
        self.item: list[CoverageEligibilityResponseInsuranceItem] | None = None
        """ Benefits and authorization details.
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("inforce", "inforce", bool, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ Benefits and authorization details.
    
    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizationRequired: bool | None = None
        """ Authorization required flag.
        Type `bool`. """
        
        self.authorizationSupporting: list[codeableconcept.CodeableConcept] | None = None
        """ Type of required supporting materials.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.authorizationUrl: str | None = None
        """ Preauthorization requirements endpoint.
        Type `str`. """
        
        self.benefit: list[CoverageEligibilityResponseInsuranceItemBenefit] | None = None
        """ Benefit Summary.
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Description of the benefit or services covered.
        Type `str`. """
        
        self.excluded: bool | None = None
        """ Excluded from the plan.
        Type `bool`. """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Short name for the benefit.
        Type `str`. """
        
        self.network: codeableconcept.CodeableConcept | None = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Performing practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.term: codeableconcept.CodeableConcept | None = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit: codeableconcept.CodeableConcept | None = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsuranceItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", codeableconcept.CodeableConcept, True, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits used to date.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItemBenefit"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney: money.Money | None = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.allowedString: str | None = None
        """ Benefits allowed.
        Type `str`. """
        
        self.allowedUnsignedInt: int | None = None
        """ Benefits allowed.
        Type `int`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usedMoney: money.Money | None = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedString: str | None = None
        """ Benefits used.
        Type `str`. """
        
        self.usedUnsignedInt: int | None = None
        """ Benefits used.
        Type `int`. """
        
        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedString", "usedString", str, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
