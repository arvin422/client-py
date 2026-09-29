# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Questionnaire).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Questionnaire(domainresource.DomainResource):
    """ A structured set of questions.
    
    A structured set of questions intended to guide the collection of answers
    from end-users. Questionnaires provide detailed control over order,
    presentation, phraseology and grouping to allow coherent, consistent data
    collection.
    """
    
    resource_type = "Questionnaire"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate: fhirdate.FHIRDate | None = None
        """ When the questionnaire was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code: list[coding.Coding] | None = None
        """ Concept that represents the overall questionnaire.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.contact: list[contactdetail.ContactDetail] | None = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright: str | None = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.derivedFrom: list[str | None] | None = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        
        self.description: str | None = None
        """ Natural language description of the questionnaire.
        Type `str`. """
        
        self.effectivePeriod: period.Period | None = None
        """ When the questionnaire is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Additional identifier for the questionnaire.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item: list[QuestionnaireItem] | None = None
        """ Questions and sections within the Questionnaire.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for questionnaire (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate: fhirdate.FHIRDate | None = None
        """ When the questionnaire was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name: str | None = None
        """ Name for this questionnaire (computer friendly).
        Type `str`. """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose: str | None = None
        """ Why this questionnaire is defined.
        Type `str`. """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.subjectType: list[str | None] | None = None
        """ Resource that can be subject of QuestionnaireResponse.
        List of `str` items. """
        
        self.title: str | None = None
        """ Name for this questionnaire (human friendly).
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical identifier for this questionnaire, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the questionnaire.
        Type `str`. """
        
        super(Questionnaire, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Questionnaire, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("derivedFrom", "derivedFrom", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectType", "subjectType", str, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class QuestionnaireItem(backboneelement.BackboneElement):
    """ Questions and sections within the Questionnaire.
    
    A particular question, question grouping or display text that is part of
    the questionnaire.
    """
    
    resource_type = "QuestionnaireItem"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerOption: list[QuestionnaireItemAnswerOption] | None = None
        """ Permitted answer.
        List of `QuestionnaireItemAnswerOption` items (represented as `dict` in JSON). """
        
        self.answerValueSet: str | None = None
        """ Valueset containing permitted answers.
        Type `str`. """
        
        self.code: list[coding.Coding] | None = None
        """ Corresponding concept for this item in a terminology.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.definition: str | None = None
        """ ElementDefinition - details for the item.
        Type `str`. """
        
        self.enableBehavior: str | None = None
        """ all | any.
        Type `str`. """
        
        self.enableWhen: list[QuestionnaireItemEnableWhen] | None = None
        """ Only allow data when.
        List of `QuestionnaireItemEnableWhen` items (represented as `dict` in JSON). """
        
        self.initial: list[QuestionnaireItemInitial] | None = None
        """ Initial value(s) when item is first rendered.
        List of `QuestionnaireItemInitial` items (represented as `dict` in JSON). """
        
        self.item: list[QuestionnaireItem] | None = None
        """ Nested questionnaire items.
        List of `QuestionnaireItem` items (represented as `dict` in JSON). """
        
        self.linkId: str | None = None
        """ Unique id for item in questionnaire.
        Type `str`. """
        
        self.maxLength: int | None = None
        """ No more than this many characters.
        Type `int`. """
        
        self.prefix: str | None = None
        """ E.g. "1(a)", "2.5.3".
        Type `str`. """
        
        self.readOnly: bool | None = None
        """ Don't allow human editing.
        Type `bool`. """
        
        self.repeats: bool | None = None
        """ Whether the item may repeat.
        Type `bool`. """
        
        self.required: bool | None = None
        """ Whether the item must be included in data results.
        Type `bool`. """
        
        self.text: str | None = None
        """ Primary text for the item.
        Type `str`. """
        
        self.type: str | None = None
        """ group | display | boolean | decimal | integer | date | dateTime +.
        Type `str`. """
        
        super(QuestionnaireItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(QuestionnaireItem, self).elementProperties()
        js.extend([
            ("answerOption", "answerOption", QuestionnaireItemAnswerOption, True, None, False),
            ("answerValueSet", "answerValueSet", str, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("enableBehavior", "enableBehavior", str, False, None, False),
            ("enableWhen", "enableWhen", QuestionnaireItemEnableWhen, True, None, False),
            ("initial", "initial", QuestionnaireItemInitial, True, None, False),
            ("item", "item", QuestionnaireItem, True, None, False),
            ("linkId", "linkId", str, False, None, True),
            ("maxLength", "maxLength", int, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("readOnly", "readOnly", bool, False, None, False),
            ("repeats", "repeats", bool, False, None, False),
            ("required", "required", bool, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    """ Permitted answer.
    
    One of the permitted answers for a "choice" or "open-choice" question.
    """
    
    resource_type = "QuestionnaireItemAnswerOption"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.initialSelected: bool | None = None
        """ Whether option is selected by default.
        Type `bool`. """
        
        self.valueCoding: coding.Coding | None = None
        """ Answer value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ Answer value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Answer value.
        Type `int`. """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Answer value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Answer value.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Answer value.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        super(QuestionnaireItemAnswerOption, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(QuestionnaireItemAnswerOption, self).elementProperties()
        js.extend([
            ("initialSelected", "initialSelected", bool, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
        ])
        return js


class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    """ Only allow data when.
    
    A constraint indicating that this item should only be enabled
    (displayed/allow answers to be captured) when the specified condition is
    true.
    """
    
    resource_type = "QuestionnaireItemEnableWhen"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answerBoolean: bool | None = None
        """ Value for question comparison based on operator.
        Type `bool`. """
        
        self.answerCoding: coding.Coding | None = None
        """ Value for question comparison based on operator.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.answerDate: fhirdate.FHIRDate | None = None
        """ Value for question comparison based on operator.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.answerDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Value for question comparison based on operator.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.answerDecimal: float | None = None
        """ Value for question comparison based on operator.
        Type `float`. """
        
        self.answerInteger: int | None = None
        """ Value for question comparison based on operator.
        Type `int`. """
        
        self.answerQuantity: quantity.Quantity | None = None
        """ Value for question comparison based on operator.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.answerReference: fhirreference.FHIRReference | None = None
        """ Value for question comparison based on operator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.answerString: str | None = None
        """ Value for question comparison based on operator.
        Type `str`. """
        
        self.answerTime: fhirtime.FHIRTime | None = None
        """ Value for question comparison based on operator.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.operator: str | None = None
        """ exists | = | != | > | < | >= | <=.
        Type `str`. """
        
        self.question: str | None = None
        """ Question that determines whether item is enabled.
        Type `str`. """
        
        super(QuestionnaireItemEnableWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(QuestionnaireItemEnableWhen, self).elementProperties()
        js.extend([
            ("answerBoolean", "answerBoolean", bool, False, "answer", True),
            ("answerCoding", "answerCoding", coding.Coding, False, "answer", True),
            ("answerDate", "answerDate", fhirdate.FHIRDate, False, "answer", True),
            ("answerDateTime", "answerDateTime", fhirdatetime.FHIRDateTime, False, "answer", True),
            ("answerDecimal", "answerDecimal", float, False, "answer", True),
            ("answerInteger", "answerInteger", int, False, "answer", True),
            ("answerQuantity", "answerQuantity", quantity.Quantity, False, "answer", True),
            ("answerReference", "answerReference", fhirreference.FHIRReference, False, "answer", True),
            ("answerString", "answerString", str, False, "answer", True),
            ("answerTime", "answerTime", fhirtime.FHIRTime, False, "answer", True),
            ("operator", "operator", str, False, None, True),
            ("question", "question", str, False, None, True),
        ])
        return js


class QuestionnaireItemInitial(backboneelement.BackboneElement):
    """ Initial value(s) when item is first rendered.
    
    One or more values that should be pre-populated in the answer when
    initially rendering the questionnaire for user input.
    """
    
    resource_type = "QuestionnaireItemInitial"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ Actual value for initializing the question.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean: bool | None = None
        """ Actual value for initializing the question.
        Type `bool`. """
        
        self.valueCoding: coding.Coding | None = None
        """ Actual value for initializing the question.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ Actual value for initializing the question.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Actual value for initializing the question.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal: float | None = None
        """ Actual value for initializing the question.
        Type `float`. """
        
        self.valueInteger: int | None = None
        """ Actual value for initializing the question.
        Type `int`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Actual value for initializing the question.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Actual value for initializing the question.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Actual value for initializing the question.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Actual value for initializing the question.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUri: str | None = None
        """ Actual value for initializing the question.
        Type `str`. """
        
        super(QuestionnaireItemInitial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(QuestionnaireItemInitial, self).elementProperties()
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


from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period
from . import quantity
from . import usagecontext
