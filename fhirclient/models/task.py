# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Task).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    
    resource_type = "Task"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn: fhirdatetime.FHIRDateTime | None = None
        """ Task Creation Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.basedOn: list[fhirreference.FHIRReference] | None = None
        """ Request fulfilled by this task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.businessStatus: codeableconcept.CodeableConcept | None = None
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code: codeableconcept.CodeableConcept | None = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Human-readable explanation of task.
        Type `str`. """
        
        self.encounter: fhirreference.FHIRReference | None = None
        """ Healthcare event during which this task originated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.executionPeriod: period.Period | None = None
        """ Start and end time of execution.
        Type `Period` (represented as `dict` in JSON). """
        
        self.focus: fhirreference.FHIRReference | None = None
        """ What task is acting on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.for_fhir: fhirreference.FHIRReference | None = None
        """ Beneficiary of the Task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier: identifier.Identifier | None = None
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Task Instance Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.input: list[TaskInput] | None = None
        """ Information used to perform task.
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical: str | None = None
        """ Formal definition of task.
        Type `str`. """
        
        self.instantiatesUri: str | None = None
        """ Formal definition of task.
        Type `str`. """
        
        self.insurance: list[fhirreference.FHIRReference] | None = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent: str | None = None
        """ unknown | proposal | plan | order | original-order | reflex-order |
        filler-order | instance-order | option.
        Type `str`. """
        
        self.lastModified: fhirdatetime.FHIRDateTime | None = None
        """ Task Last Modified Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.location: fhirreference.FHIRReference | None = None
        """ Where task occurs.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note: list[annotation.Annotation] | None = None
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.output: list[TaskOutput] | None = None
        """ Information produced as part of task.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        self.owner: fhirreference.FHIRReference | None = None
        """ Responsible individual.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf: list[fhirreference.FHIRReference] | None = None
        """ Composite task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType: list[codeableconcept.CodeableConcept] | None = None
        """ Requested performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority: str | None = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.reasonCode: codeableconcept.CodeableConcept | None = None
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference: fhirreference.FHIRReference | None = None
        """ Why task is needed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relevantHistory: list[fhirreference.FHIRReference] | None = None
        """ Key events in history of the Task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester: fhirreference.FHIRReference | None = None
        """ Who is asking for task to be done.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.restriction: TaskRestriction | None = None
        """ Constraints on fulfillment tasks.
        Type `TaskRestriction` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | requested | received | accepted | +.
        Type `str`. """
        
        self.statusReason: codeableconcept.CodeableConcept | None = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("lastModified", "lastModified", fhirdatetime.FHIRDateTime, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.
    
    Additional information that may be needed in the execution of the task.
    """
    
    resource_type = "TaskInput"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress: address.Address | None = None
        """ Content to use in performing the task.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge: age.Age | None = None
        """ Content to use in performing the task.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation: annotation.Annotation | None = None
        """ Content to use in performing the task.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ Content to use in performing the task.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueBoolean: bool | None = None
        """ Content to use in performing the task.
        Type `bool`. """
        
        self.valueCanonical: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueCode: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Content to use in performing the task.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding: coding.Coding | None = None
        """ Content to use in performing the task.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail: contactdetail.ContactDetail | None = None
        """ Content to use in performing the task.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint: contactpoint.ContactPoint | None = None
        """ Content to use in performing the task.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor: contributor.Contributor | None = None
        """ Content to use in performing the task.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount: count.Count | None = None
        """ Content to use in performing the task.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement: datarequirement.DataRequirement | None = None
        """ Content to use in performing the task.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Content to use in performing the task.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal: float | None = None
        """ Content to use in performing the task.
        Type `float`. """
        
        self.valueDistance: distance.Distance | None = None
        """ Content to use in performing the task.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage: dosage.Dosage | None = None
        """ Content to use in performing the task.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration: duration.Duration | None = None
        """ Content to use in performing the task.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression: expression.Expression | None = None
        """ Content to use in performing the task.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName: humanname.HumanName | None = None
        """ Content to use in performing the task.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueIdentifier: identifier.Identifier | None = None
        """ Content to use in performing the task.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant: fhirinstant.FHIRInstant | None = None
        """ Content to use in performing the task.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Content to use in performing the task.
        Type `int`. """
        
        self.valueMarkdown: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueMeta: meta.Meta | None = None
        """ Content to use in performing the task.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney: money.Money | None = None
        """ Content to use in performing the task.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Content to use in performing the task.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod: period.Period | None = None
        """ Content to use in performing the task.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt: int | None = None
        """ Content to use in performing the task.
        Type `int`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Content to use in performing the task.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Content to use in performing the task.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio: ratio.Ratio | None = None
        """ Content to use in performing the task.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Content to use in performing the task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Content to use in performing the task.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData: sampleddata.SampledData | None = None
        """ Content to use in performing the task.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature: signature.Signature | None = None
        """ Content to use in performing the task.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Content to use in performing the task.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueTiming: timing.Timing | None = None
        """ Content to use in performing the task.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Content to use in performing the task.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt: int | None = None
        """ Content to use in performing the task.
        Type `int`. """
        
        self.valueUri: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueUrl: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        self.valueUsageContext: usagecontext.UsageContext | None = None
        """ Content to use in performing the task.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid: str | None = None
        """ Content to use in performing the task.
        Type `str`. """
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.
    
    Outputs produced by the Task.
    """
    
    resource_type = "TaskOutput"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Label for output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress: address.Address | None = None
        """ Result of output.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge: age.Age | None = None
        """ Result of output.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation: annotation.Annotation | None = None
        """ Result of output.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ Result of output.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueBoolean: bool | None = None
        """ Result of output.
        Type `bool`. """
        
        self.valueCanonical: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueCode: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Result of output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding: coding.Coding | None = None
        """ Result of output.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail: contactdetail.ContactDetail | None = None
        """ Result of output.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint: contactpoint.ContactPoint | None = None
        """ Result of output.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor: contributor.Contributor | None = None
        """ Result of output.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount: count.Count | None = None
        """ Result of output.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement: datarequirement.DataRequirement | None = None
        """ Result of output.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Result of output.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal: float | None = None
        """ Result of output.
        Type `float`. """
        
        self.valueDistance: distance.Distance | None = None
        """ Result of output.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage: dosage.Dosage | None = None
        """ Result of output.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration: duration.Duration | None = None
        """ Result of output.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression: expression.Expression | None = None
        """ Result of output.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName: humanname.HumanName | None = None
        """ Result of output.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueIdentifier: identifier.Identifier | None = None
        """ Result of output.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant: fhirinstant.FHIRInstant | None = None
        """ Result of output.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Result of output.
        Type `int`. """
        
        self.valueMarkdown: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueMeta: meta.Meta | None = None
        """ Result of output.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney: money.Money | None = None
        """ Result of output.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Result of output.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod: period.Period | None = None
        """ Result of output.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt: int | None = None
        """ Result of output.
        Type `int`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Result of output.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Result of output.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio: ratio.Ratio | None = None
        """ Result of output.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Result of output.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Result of output.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData: sampleddata.SampledData | None = None
        """ Result of output.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature: signature.Signature | None = None
        """ Result of output.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Result of output.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueTiming: timing.Timing | None = None
        """ Result of output.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Result of output.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt: int | None = None
        """ Result of output.
        Type `int`. """
        
        self.valueUri: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueUrl: str | None = None
        """ Result of output.
        Type `str`. """
        
        self.valueUsageContext: usagecontext.UsageContext | None = None
        """ Result of output.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid: str | None = None
        """ Result of output.
        Type `str`. """
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js


class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.
    
    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    
    resource_type = "TaskRestriction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period: period.Period | None = None
        """ When fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """
        
        self.recipient: list[fhirreference.FHIRReference] | None = None
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.repetitions: int | None = None
        """ How many times to repeat.
        Type `int`. """
        
        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("repetitions", "repetitions", int, False, None, False),
        ])
        return js


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import fhirtime
from . import humanname
from . import identifier
from . import meta
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext
