# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Claim).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Claim(domainresource.DomainResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of professional services and products which have
    been provided, or are to be provided, to a patient which is sent to an
    insurer for reimbursement.
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident: ClaimAccident | None = None
        """ Details of the event.
        Type `ClaimAccident` (represented as `dict` in JSON). """
        
        self.billablePeriod: period.Period | None = None
        """ Relevant time frame for the claim.
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam: list[ClaimCareTeam] | None = None
        """ Members of the care team.
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Resource creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.diagnosis: list[ClaimDiagnosis] | None = None
        """ Pertinent diagnosis information.
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.enterer: fhirreference.FHIRReference | None = None
        """ Author of the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility: fhirreference.FHIRReference | None = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fundsReserve: codeableconcept.CodeableConcept | None = None
        """ For whom to reserve funds.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for claim.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance: list[ClaimInsurance] | None = None
        """ Patient insurance information.
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        
        self.insurer: fhirreference.FHIRReference | None = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item: list[ClaimItem] | None = None
        """ Product or service provided.
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.originalPrescription: fhirreference.FHIRReference | None = None
        """ Original prescription if superseded by fulfiller.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ The recipient of the products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee: ClaimPayee | None = None
        """ Recipient of benefits payable.
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescription: fhirreference.FHIRReference | None = None
        """ Prescription authorizing services and products.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority: codeableconcept.CodeableConcept | None = None
        """ Desired processing ugency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure: list[ClaimProcedure] | None = None
        """ Clinical procedures performed.
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
        self.provider: fhirreference.FHIRReference | None = None
        """ Party responsible for the claim.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referral: fhirreference.FHIRReference | None = None
        """ Treatment referral.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.related: list[ClaimRelated] | None = None
        """ Prior or corollary claims.
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.subType: codeableconcept.CodeableConcept | None = None
        """ More granular claim type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.supportingInfo: list[ClaimSupportingInfo] | None = None
        """ Supporting information.
        List of `ClaimSupportingInfo` items (represented as `dict` in JSON). """
        
        self.total: money.Money | None = None
        """ Total claim cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Category or discipline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use: str | None = None
        """ claim | preauthorization | predetermination.
        Type `str`. """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, True),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, True),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False),
            ("total", "total", money.Money, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


from . import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ Details of the event.
    
    Details of an accident which resulted in injuries which required the
    products and services listed in the claim.
    """
    
    resource_type = "ClaimAccident"
    
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
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ Members of the care team.
    
    The members of the team who provided the products and services.
    """
    
    resource_type = "ClaimCareTeam"
    
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
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ Pertinent diagnosis information.
    
    Information about diagnoses relevant to the claim items.
    """
    
    resource_type = "ClaimDiagnosis"
    
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
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ClaimInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """
    
    resource_type = "ClaimInsurance"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement: str | None = None
        """ Additional provider contract number.
        Type `str`. """
        
        self.claimResponse: fhirreference.FHIRReference | None = None
        """ Adjudication results.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage: fhirreference.FHIRReference | None = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focal: bool | None = None
        """ Coverage to be used for adjudication.
        Type `bool`. """
        
        self.identifier: identifier.Identifier | None = None
        """ Pre-assigned Claim number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.preAuthRef: list[str | None] | None = None
        """ Prior authorization reference number.
        List of `str` items. """
        
        self.sequence: int | None = None
        """ Insurance instance identifier.
        Type `int`. """
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim line. Either a simple  product or service or a 'group' of details
    which can each be a simple items or groups of sub-details.
    """
    
    resource_type = "ClaimItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite: codeableconcept.CodeableConcept | None = None
        """ Anatomical location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamSequence: list[int | None] | None = None
        """ Applicable careTeam members.
        List of `int` items. """
        
        self.category: codeableconcept.CodeableConcept | None = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail: list[ClaimItemDetail] | None = None
        """ Product or service provided.
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
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
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
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


class ClaimItemDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    resource_type = "ClaimItemDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.subDetail: list[ClaimItemDetailSubDetail] | None = None
        """ Product or service provided.
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    """ Product or service provided.
    
    A claim detail line. Either a simple (a product or service) or a 'group' of
    sub-details which are simple items.
    """
    
    resource_type = "ClaimItemDetailSubDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.udi: list[fhirreference.FHIRReference] | None = None
        """ Unique device identifier.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.unitPrice: money.Money | None = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
    """ Recipient of benefits payable.
    
    The party to be reimbursed for cost of the products and services according
    to the terms of the policy.
    """
    
    resource_type = "ClaimPayee"
    
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
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ Clinical procedures performed.
    
    Procedures performed on the patient relevant to the billing items with the
    claim.
    """
    
    resource_type = "ClaimProcedure"
    
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
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ Prior or corollary claims.
    
    Other claims which are related to this claim such as prior submissions or
    claims for related services or for the same event.
    """
    
    resource_type = "ClaimRelated"
    
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
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "ClaimSupportingInfo"
    
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
        
        self.reason: codeableconcept.CodeableConcept | None = None
        """ Explanation for the information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
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


from . import address
from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity
