# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_type = "ExplanationOfBenefit"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident: ExplanationOfBenefitAccident | None = None
        """ Details of the event.
        Type `ExplanationOfBenefitAccident` (represented as `dict` in JSON). """
        
        self.addItem: list[ExplanationOfBenefitAddItem] | None = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON). """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Header-level adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.benefitBalance: list[ExplanationOfBenefitBenefitBalance] | None = None
        """ Balance by Benefit Category.
        List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON). """
        
        self.benefitPeriod: period.Period | None = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """
        
        self.billablePeriod: period.Period | None = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam: list[ExplanationOfBenefitCareTeam] | None = None
        """ Care Team members.
        List of `ExplanationOfBenefitCareTeam` items (represented as `dict` in JSON). """
        
        self.claim: fhirreference.FHIRReference | None = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.claimResponse: fhirreference.FHIRReference | None = None
        """ Claim response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.diagnosis: list[ExplanationOfBenefitDiagnosis] | None = None
        """ Pertinent diagnosis information.
        List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON). """
        
        self.disposition: str | None = None
        """ Disposition Message.
        Type `str`. """
        
        self.enterer: fhirreference.FHIRReference | None = None
        """ Author of the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility: fhirreference.FHIRReference | None = None
        """ Servicing Facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.form: attachment.Attachment | None = None
        """ Printed reference or actual form.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.formCode: codeableconcept.CodeableConcept | None = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fundsReserve: codeableconcept.CodeableConcept | None = None
        """ Funds reserved status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fundsReserveRequested: codeableconcept.CodeableConcept | None = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for the resource.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance: list[ExplanationOfBenefitInsurance] | None = None
        """ Patient insurance information.
        List of `ExplanationOfBenefitInsurance` items (represented as `dict` in JSON). """
        
        self.insurer: fhirreference.FHIRReference | None = None
        """ Party responsible for reimbursement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item: list[ExplanationOfBenefitItem] | None = None
        """ Product or service provided.
        List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON). """
        
        self.originalPrescription: fhirreference.FHIRReference | None = None
        """ Original prescription if superceded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome: str | None = None
        """ queued | complete | error | partial.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ The recipient of the products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee: ExplanationOfBenefitPayee | None = None
        """ Recipient of benefits payable.
        Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON). """
        
        self.payment: ExplanationOfBenefitPayment | None = None
        """ Payment Details.
        Type `ExplanationOfBenefitPayment` (represented as `dict` in JSON). """
        
        self.preAuthRef: list[str | None] | None = None
        """ Preauthorization reference.
        List of `str` items. """
        
        self.preAuthRefPeriod: list[period.Period] | None = None
        """ Preauthorization in-effect period.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.precedence: int | None = None
        """ Precedence (primary, secondary, etc.).
        Type `int`. """
        
        self.prescription: fhirreference.FHIRReference | None = None
        """ Prescription authorizing services or products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority: codeableconcept.CodeableConcept | None = None
        """ Desired processing urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure: list[ExplanationOfBenefitProcedure] | None = None
        """ Clinical procedures performed.
        List of `ExplanationOfBenefitProcedure` items (represented as `dict` in JSON). """
        
        self.processNote: list[ExplanationOfBenefitProcessNote] | None = None
        """ Note concerning adjudication.
        List of `ExplanationOfBenefitProcessNote` items (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referral: fhirreference.FHIRReference | None = None
        """ Treatment Referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.related: list[ExplanationOfBenefitRelated] | None = None
        """ Prior or corollary claims.
        List of `ExplanationOfBenefitRelated` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subType: codeableconcept.CodeableConcept | None = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.supportingInfo: list[ExplanationOfBenefitSupportingInfo] | None = None
        """ Supporting information.
        List of `ExplanationOfBenefitSupportingInfo` items (represented as `dict` in JSON). """
        
        self.total: list[ExplanationOfBenefitTotal] | None = None
        """ Adjudication totals.
        List of `ExplanationOfBenefitTotal` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Category or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use: str | None = None
        """ claim | preauthorization | predetermination.
        Type `str`. """
        
        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accident", "accident", ExplanationOfBenefitAccident, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ExplanationOfBenefitCareTeam, True, None, False),
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("form", "form", attachment.Attachment, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("fundsReserveRequested", "fundsReserveRequested", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ExplanationOfBenefitInsurance, True, None, True),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("payment", "payment", ExplanationOfBenefitPayment, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("preAuthRefPeriod", "preAuthRefPeriod", period.Period, True, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("procedure", "procedure", ExplanationOfBenefitProcedure, True, None, False),
            ("processNote", "processNote", ExplanationOfBenefitProcessNote, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ExplanationOfBenefitRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ExplanationOfBenefitSupportingInfo, True, None, False),
            ("total", "total", ExplanationOfBenefitTotal, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


from . import backboneelement

class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    """ Details of the event.
    
    Details of a accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    
    resource_type = "ExplanationOfBenefitAccident"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date: fhirdate.FHIRDate | None = None
        """ When the incident occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.locationAddress: address.Address | None = None
        """ Where the event occurred.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference: fhirreference.FHIRReference | None = None
        """ Where the event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ The nature of the accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first-tier service adjudications for payor added product or service
    lines.
    """
    
    resource_type = "ExplanationOfBenefitAddItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail: list[ExplanationOfBenefitAddItemDetail] | None = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON). """
        
        self.detailSequence: list[int | None] | None = None
        """ Detail sequence number.
        List of `int` items. """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.itemSequence: list[int | None] | None = None
        """ Item sequence number.
        List of `int` items. """
        
        self.locationAddress: address.Address | None = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference: fhirreference.FHIRReference | None = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.programCode: list[codeableconcept.CodeableConcept] | None = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider: list[fhirreference.FHIRReference] | None = None
        """ Authorized providers.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.servicedDate: fhirdate.FHIRDate | None = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod: period.Period | None = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subDetailSequence: list[int | None] | None = None
        """ Subdetail sequence number.
        List of `int` items. """
        
        self.subSite: list[codeableconcept.CodeableConcept] | None = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("detailSequence", "detailSequence", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("itemSequence", "itemSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subDetailSequence", "subDetailSequence", int, True, None, False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The second-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.subDetail: list[ExplanationOfBenefitAddItemDetailSubDetail] | None = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("subDetail", "subDetail", ExplanationOfBenefitAddItemDetailSubDetail, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The third-tier service adjudications for payor added services.
    """
    
    resource_type = "ExplanationOfBenefitAddItemDetailSubDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitAddItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Description of the benefit or services covered.
        Type `str`. """
        
        self.excluded: bool | None = None
        """ Excluded from the plan.
        Type `bool`. """
        
        self.financial: list[ExplanationOfBenefitBenefitBalanceFinancial] | None = None
        """ Benefit Summary.
        List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Short name for the benefit.
        Type `str`. """
        
        self.network: codeableconcept.CodeableConcept | None = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.term: codeableconcept.CodeableConcept | None = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit: codeableconcept.CodeableConcept | None = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_type = "ExplanationOfBenefitBenefitBalanceFinancial"
    
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
        
        self.usedUnsignedInt: int | None = None
        """ Benefits used.
        Type `int`. """
        
        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
        ])
        return js


class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    """ Care Team members.
    
    The members of the team who provided the products and services.
    """
    
    resource_type = "ExplanationOfBenefitCareTeam"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Practitioner or organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.qualification: codeableconcept.CodeableConcept | None = None
        """ Practitioner credential or specialization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.responsible: bool | None = None
        """ Indicator of the lead practitioner.
        Type `bool`. """
        
        self.role: codeableconcept.CodeableConcept | None = None
        """ Function within the team.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Order of care team.
        Type `int`. """
        
        super(ExplanationOfBenefitCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    
    Information about diagnoses relevant to the claim items.
    """
    
    resource_type = "ExplanationOfBenefitDiagnosis"
    
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
        
        self.onAdmission: codeableconcept.CodeableConcept | None = None
        """ Present on admission.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.packageCode: codeableconcept.CodeableConcept | None = None
        """ Package billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Diagnosis instance identifier.
        Type `int`. """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Timing or nature of the diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    resource_type = "ExplanationOfBenefitInsurance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage: fhirreference.FHIRReference | None = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal: bool | None = None
        """ Coverage to be used for adjudication.
        Type `bool`. """
        
        self.preAuthRef: list[str | None] | None = None
        """ Prior authorization reference number.
        List of `str` items. """
        
        super(ExplanationOfBenefitInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
        ])
        return js


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """
    
    resource_type = "ExplanationOfBenefitItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamSequence: list[int | None] | None = None
        """ Applicable care team members.
        List of `int` items. """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail: list[ExplanationOfBenefitItemDetail] | None = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisSequence: list[int | None] | None = None
        """ Applicable diagnoses.
        List of `int` items. """
        
        self.encounter: list[fhirreference.FHIRReference] | None = None
        """ Encounters related to this billed item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.informationSequence: list[int | None] | None = None
        """ Applicable exception and supporting information.
        List of `int` items. """
        
        self.locationAddress: address.Address | None = None
        """ Place of service or where product was supplied.
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Place of service or where product was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference: fhirreference.FHIRReference | None = None
        """ Place of service or where product was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.procedureSequence: list[int | None] | None = None
        """ Applicable procedures.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.programCode: list[codeableconcept.CodeableConcept] | None = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue: codeableconcept.CodeableConcept | None = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Item instance identifier.
        Type `int`. """
        
        self.servicedDate: fhirdate.FHIRDate | None = None
        """ Date or dates of service or product delivery.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod: period.Period | None = None
        """ Date or dates of service or product delivery.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite: list[codeableconcept.CodeableConcept] | None = None
        """ Anatomical sub-location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """
    
    resource_type = "ExplanationOfBenefitItemAdjudication"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount: money.Money | None = None
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Type of adjudication information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason: codeableconcept.CodeableConcept | None = None
        """ Explanation of adjudication outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value: float | None = None
        """ Non-monitary value.
        Type `float`. """
        
        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Detail level adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.programCode: list[codeableconcept.CodeableConcept] | None = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue: codeableconcept.CodeableConcept | None = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Product or service provided.
        Type `int`. """
        
        self.subDetail: list[ExplanationOfBenefitItemDetailSubDetail] | None = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third-tier of goods and services.
    """
    
    resource_type = "ExplanationOfBenefitItemDetailSubDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication: list[ExplanationOfBenefitItemAdjudication] | None = None
        """ Subdetail level adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier: list[codeableconcept.CodeableConcept] | None = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.net: money.Money | None = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.noteNumber: list[int | None] | None = None
        """ Applicable note numbers.
        List of `int` items. """
        
        self.productOrService: codeableconcept.CodeableConcept | None = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.programCode: list[codeableconcept.CodeableConcept] | None = None
        """ Program the product or service is provided under.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.revenue: codeableconcept.CodeableConcept | None = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Product or service provided.
        Type `int`. """
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    
    resource_type = "ExplanationOfBenefitPayee"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party: fhirreference.FHIRReference | None = None
        """ Recipient reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Category of recipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
    """ Payment Details.
    
    Payment details for the adjudication of the claim.
    """
    
    resource_type = "ExplanationOfBenefitPayment"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment: money.Money | None = None
        """ Payment adjustment for non-claim issues.
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason: codeableconcept.CodeableConcept | None = None
        """ Explanation for the variance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount: money.Money | None = None
        """ Payable amount after adjustment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date: fhirdate.FHIRDate | None = None
        """ Expected date of payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Partial or complete payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitPayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitPayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    
    resource_type = "ExplanationOfBenefitProcedure"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Specific clinical procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference: fhirreference.FHIRReference | None = None
        """ Specific clinical procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Procedure instance identifier.
        Type `int`. """
        
        self.type: list[codeableconcept.CodeableConcept] | None = None
        """ Category of Procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    """ Note concerning adjudication.
    
    A note that describes or explains adjudication results in a human readable
    form.
    """
    
    resource_type = "ExplanationOfBenefitProcessNote"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language: codeableconcept.CodeableConcept | None = None
        """ Language of the text.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number: int | None = None
        """ Note instance identifier.
        Type `int`. """
        
        self.text: str | None = None
        """ Note explanatory text.
        Type `str`. """
        
        self.type: str | None = None
        """ display | print | printoper.
        Type `str`. """
        
        super(ExplanationOfBenefitProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    
    resource_type = "ExplanationOfBenefitRelated"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim: fhirreference.FHIRReference | None = None
        """ Reference to the related claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference: identifier.Identifier | None = None
        """ File or case reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship: codeableconcept.CodeableConcept | None = None
        """ How the reference claim is related.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "ExplanationOfBenefitSupportingInfo"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Classification of the supplied information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Type of information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason: coding.Coding | None = None
        """ Explanation for the information.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Information instance identifier.
        Type `int`. """
        
        self.timingDate: fhirdate.FHIRDate | None = None
        """ When it occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod: period.Period | None = None
        """ When it occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ Data to be provided.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ Data to be provided.
        Type `bool`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Data to be provided.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Data to be provided.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Data to be provided.
        Type `str`. """
        
        super(ExplanationOfBenefitSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    """ Adjudication totals.
    
    Categorized monetary totals for the adjudication.
    """
    
    resource_type = "ExplanationOfBenefitTotal"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount: money.Money | None = None
        """ Financial total for the category.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Type of adjudication information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitTotal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ExplanationOfBenefitTotal, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
