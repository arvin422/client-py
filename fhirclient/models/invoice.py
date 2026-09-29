# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Invoice).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Invoice(domainresource.DomainResource):
    """ Invoice containing ChargeItems from an Account.
    
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    
    resource_type = "Invoice"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account: fhirreference.FHIRReference | None = None
        """ Account that is being balanced.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.cancelledReason: str | None = None
        """ Reason for cancellation of this Invoice.
        Type `str`. """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Invoice date / posting date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer: fhirreference.FHIRReference | None = None
        """ Issuing Organization of Invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lineItem: list[InvoiceLineItem] | None = None
        """ Line items of this Invoice.
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments made about the invoice.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.participant: list[InvoiceParticipant] | None = None
        """ Participant in creation of this Invoice.
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """
        
        self.paymentTerms: str | None = None
        """ Payment details.
        Type `str`. """
        
        self.recipient: fhirreference.FHIRReference | None = None
        """ Recipient of this invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | issued | balanced | cancelled | entered-in-error.
        Type `str`. """
        
        self.subject: fhirreference.FHIRReference | None = None
        """ Recipient(s) of goods and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.totalGross: money.Money | None = None
        """ Gross total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalNet: money.Money | None = None
        """ Net total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalPriceComponent: list[InvoiceLineItemPriceComponent] | None = None
        """ Components of Invoice total.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Type of Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, False, None, False),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("totalGross", "totalGross", money.Money, False, None, False),
            ("totalNet", "totalNet", money.Money, False, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class InvoiceLineItem(backboneelement.BackboneElement):
    """ Line items of this Invoice.
    
    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    
    resource_type = "InvoiceLineItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chargeItemCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.chargeItemReference: fhirreference.FHIRReference | None = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priceComponent: list[InvoiceLineItemPriceComponent] | None = None
        """ Components of total line item price.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.sequence: int | None = None
        """ Sequence number of line item.
        Type `int`. """
        
        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", codeableconcept.CodeableConcept, False, "chargeItem", True),
            ("chargeItemReference", "chargeItemReference", fhirreference.FHIRReference, False, "chargeItem", True),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("sequence", "sequence", int, False, None, False),
        ])
        return js


class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """
    
    resource_type = "InvoiceLineItemPriceComponent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount: money.Money | None = None
        """ Monetary amount associated with this component.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor: float | None = None
        """ Factor used for calculating this component.
        Type `float`. """
        
        self.type: str | None = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """
        
        super(InvoiceLineItemPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class InvoiceParticipant(backboneelement.BackboneElement):
    """ Participant in creation of this Invoice.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    resource_type = "InvoiceParticipant"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor: fhirreference.FHIRReference | None = None
        """ Individual who was involved.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role: codeableconcept.CodeableConcept | None = None
        """ Type of involvement in creation of this Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
