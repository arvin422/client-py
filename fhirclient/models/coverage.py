# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coverage).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.beneficiary: fhirreference.FHIRReference | None = None
        """ Plan beneficiary.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.class_fhir: list[CoverageClass] | None = None
        """ Additional coverage classifications.
        List of `CoverageClass` items (represented as `dict` in JSON). """
        
        self.contract: list[fhirreference.FHIRReference] | None = None
        """ Contract details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.costToBeneficiary: list[CoverageCostToBeneficiary] | None = None
        """ Patient payments for services/products.
        List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON). """
        
        self.dependent: str | None = None
        """ Dependent number.
        Type `str`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for the coverage.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.network: str | None = None
        """ Insurer network.
        Type `str`. """
        
        self.order: int | None = None
        """ Relative order of the coverage.
        Type `int`. """
        
        self.payor: list[fhirreference.FHIRReference] | None = None
        """ Issuer of the policy.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.policyHolder: fhirreference.FHIRReference | None = None
        """ Owner of the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship: codeableconcept.CodeableConcept | None = None
        """ Beneficiary relationship to the subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subrogation: bool | None = None
        """ Reimbursement to insurer.
        Type `bool`. """
        
        self.subscriber: fhirreference.FHIRReference | None = None
        """ Subscriber to the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subscriberId: str | None = None
        """ ID assigned to the subscriber.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Coverage category such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", str, False, None, False),
            ("order", "order", int, False, None, False),
            ("payor", "payor", fhirreference.FHIRReference, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subrogation", "subrogation", bool, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    
    A suite of underwriter specific classifiers.
    """
    
    resource_type = "CoverageClass"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name: str | None = None
        """ Human readable description of the type and value.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of class such as 'group' or 'plan'.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: str | None = None
        """ Value associated with the type.
        Type `str`. """
        
        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.
    
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    
    resource_type = "CoverageCostToBeneficiary"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exception: list[CoverageCostToBeneficiaryException] | None = None
        """ Exceptions for patient payments.
        List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Cost category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueMoney: money.Money | None = None
        """ The amount or percentage due from the beneficiary.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ The amount or percentage due from the beneficiary.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
        ])
        return js


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.
    
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    
    resource_type = "CoverageCostToBeneficiaryException"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period: period.Period | None = None
        """ The effective period of the exception.
        Type `Period` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Exception category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiaryException, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
