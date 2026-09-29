# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/InsurancePlan).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class InsurancePlan(domainresource.DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    
    resource_type = "InsurancePlan"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administeredBy: fhirreference.FHIRReference | None = None
        """ Product administrator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.alias: list[str | None] | None = None
        """ Alternate names.
        List of `str` items. """
        
        self.contact: list[InsurancePlanContact] | None = None
        """ Contact for the product.
        List of `InsurancePlanContact` items (represented as `dict` in JSON). """
        
        self.coverage: list[InsurancePlanCoverage] | None = None
        """ Coverage details.
        List of `InsurancePlanCoverage` items (represented as `dict` in JSON). """
        
        self.coverageArea: list[fhirreference.FHIRReference] | None = None
        """ Where product applies.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.endpoint: list[fhirreference.FHIRReference] | None = None
        """ Technical endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for Product.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Official name.
        Type `str`. """
        
        self.network: list[fhirreference.FHIRReference] | None = None
        """ What networks are Included.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.ownedBy: fhirreference.FHIRReference | None = None
        """ Plan issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ When the product is available.
        Type `Period` (represented as `dict` in JSON). """
        
        self.plan: list[InsurancePlanPlan] | None = None
        """ Plan details.
        List of `InsurancePlanPlan` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Kind of product.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(InsurancePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("administeredBy", "administeredBy", fhirreference.FHIRReference, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("ownedBy", "ownedBy", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class InsurancePlanContact(backboneelement.BackboneElement):
    """ Contact for the product.
    
    The contact for the health insurance product for a certain purpose.
    """
    
    resource_type = "InsurancePlanContact"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address: address.Address | None = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        self.name: humanname.HumanName | None = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose: codeableconcept.CodeableConcept | None = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom: list[contactpoint.ContactPoint] | None = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(InsurancePlanContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """ Coverage details.
    
    Details about the coverage offered by the insurance product.
    """
    
    resource_type = "InsurancePlanCoverage"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit: list[InsurancePlanCoverageBenefit] | None = None
        """ List of benefits.
        List of `InsurancePlanCoverageBenefit` items (represented as `dict` in JSON). """
        
        self.network: list[fhirreference.FHIRReference] | None = None
        """ What networks provide coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of coverage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """ List of benefits.
    
    Specific benefits under this type of coverage.
    """
    
    resource_type = "InsurancePlanCoverageBenefit"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.limit: list[InsurancePlanCoverageBenefitLimit] | None = None
        """ Benefit limits.
        List of `InsurancePlanCoverageBenefitLimit` items (represented as `dict` in JSON). """
        
        self.requirement: str | None = None
        """ Referral requirements.
        Type `str`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverageBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """ Benefit limits.
    
    The specific limits on the benefit.
    """
    
    resource_type = "InsurancePlanCoverageBenefitLimit"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Benefit limit details.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: quantity.Quantity | None = None
        """ Maximum value allowed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverageBenefitLimit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js


class InsurancePlanPlan(backboneelement.BackboneElement):
    """ Plan details.
    
    Details about an insurance plan.
    """
    
    resource_type = "InsurancePlanPlan"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverageArea: list[fhirreference.FHIRReference] | None = None
        """ Where product applies.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.generalCost: list[InsurancePlanPlanGeneralCost] | None = None
        """ Overall costs.
        List of `InsurancePlanPlanGeneralCost` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for Product.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.network: list[fhirreference.FHIRReference] | None = None
        """ What networks provide coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specificCost: list[InsurancePlanPlanSpecificCost] | None = None
        """ Specific costs.
        List of `InsurancePlanPlanSpecificCost` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of plan.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """ Overall costs.
    
    Overall costs associated with the plan.
    """
    
    resource_type = "InsurancePlanPlanGeneralCost"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment: str | None = None
        """ Additional cost information.
        Type `str`. """
        
        self.cost: money.Money | None = None
        """ Cost value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.groupSize: int | None = None
        """ Number of enrollees.
        Type `int`. """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of cost.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanGeneralCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("cost", "cost", money.Money, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    """ Specific costs.
    
    Costs associated with the coverage provided by the product.
    """
    
    resource_type = "InsurancePlanPlanSpecificCost"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit: list[InsurancePlanPlanSpecificCostBenefit] | None = None
        """ Benefits list.
        List of `InsurancePlanPlanSpecificCostBenefit` items (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ General category of benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """ Benefits list.
    
    List of the specific benefits under this category of benefit.
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefit"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost: list[InsurancePlanPlanSpecificCostBenefitCost] | None = None
        """ List of the costs.
        List of `InsurancePlanPlanSpecificCostBenefitCost` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of specific benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCostBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """ List of the costs.
    
    List of the costs associated with a specific benefit.
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefitCost"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability: codeableconcept.CodeableConcept | None = None
        """ in-network | out-of-network | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.qualifiers: list[codeableconcept.CodeableConcept] | None = None
        """ Additional information about the cost.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of cost.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: quantity.Quantity | None = None
        """ The actual cost value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCostBenefitCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", codeableconcept.CodeableConcept, False, None, False),
            ("qualifiers", "qualifiers", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js


from . import address
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import period
from . import quantity
