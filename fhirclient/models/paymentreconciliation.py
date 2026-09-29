# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    
    resource_type = "PaymentReconciliation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created: fhirdatetime.FHIRDateTime | None = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.detail: list[PaymentReconciliationDetail] | None = None
        """ Settlement particulars.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition: str | None = None
        """ Disposition message.
        Type `str`. """
        
        self.formCode: codeableconcept.CodeableConcept | None = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for a payment reconciliation.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.outcome: str | None = None
        """ queued | complete | error | partial.
        Type `str`. """
        
        self.paymentAmount: money.Money | None = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentDate: fhirdate.FHIRDate | None = None
        """ When payment issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentIdentifier: identifier.Identifier | None = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.paymentIssuer: fhirreference.FHIRReference | None = None
        """ Party generating payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period: period.Period | None = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.processNote: list[PaymentReconciliationProcessNote] | None = None
        """ Note concerning processing.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        
        self.request: fhirreference.FHIRReference | None = None
        """ Reference to requesting resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor: fhirreference.FHIRReference | None = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("paymentAmount", "paymentAmount", money.Money, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False),
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Settlement particulars.
    
    Distribution of the payment amount for a previously acknowledged payable.
    """
    
    resource_type = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount: money.Money | None = None
        """ Amount allocated to this payable.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date: fhirdate.FHIRDate | None = None
        """ Date of commitment to pay.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Business identifier of the payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.payee: fhirreference.FHIRReference | None = None
        """ Recipient of the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.predecessor: identifier.Identifier | None = None
        """ Business identifier of the prior payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.request: fhirreference.FHIRReference | None = None
        """ Request giving rise to the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response: fhirreference.FHIRReference | None = None
        """ Response committing to a payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible: fhirreference.FHIRReference | None = None
        """ Contact for the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter: fhirreference.FHIRReference | None = None
        """ Submitter of the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Category of payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("predecessor", "predecessor", identifier.Identifier, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Note concerning processing.
    
    A note that describes or explains the processing in a human readable form.
    """
    
    resource_type = "PaymentReconciliationProcessNote"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text: str | None = None
        """ Note explanatory text.
        Type `str`. """
        
        self.type: str | None = None
        """ display | print | printoper.
        Type `str`. """
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
