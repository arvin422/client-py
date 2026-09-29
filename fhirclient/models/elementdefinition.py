# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ElementDefinition).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import backboneelement

class ElementDefinition(backboneelement.BackboneElement):
    """ Definition of an element in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_type = "ElementDefinition"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias: list[str | None] | None = None
        """ Other names.
        List of `str` items. """
        
        self.base: ElementDefinitionBase | None = None
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        
        self.binding: ElementDefinitionBinding | None = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.code: list[coding.Coding] | None = None
        """ Corresponding codes in terminologies.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.comment: str | None = None
        """ Comments about the use of this element.
        Type `str`. """
        
        self.condition: list[str | None] | None = None
        """ Reference to invariant about presence.
        List of `str` items. """
        
        self.constraint: list[ElementDefinitionConstraint] | None = None
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.contentReference: str | None = None
        """ Reference to definition of content for the element.
        Type `str`. """
        
        self.defaultValueAddress: address.Address | None = None
        """ Specified value if missing from instance.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge: age.Age | None = None
        """ Specified value if missing from instance.
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation: annotation.Annotation | None = None
        """ Specified value if missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment: attachment.Attachment | None = None
        """ Specified value if missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueBoolean: bool | None = None
        """ Specified value if missing from instance.
        Type `bool`. """
        
        self.defaultValueCanonical: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueCode: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Specified value if missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding: coding.Coding | None = None
        """ Specified value if missing from instance.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail: contactdetail.ContactDetail | None = None
        """ Specified value if missing from instance.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint: contactpoint.ContactPoint | None = None
        """ Specified value if missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor: contributor.Contributor | None = None
        """ Specified value if missing from instance.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount: count.Count | None = None
        """ Specified value if missing from instance.
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement: datarequirement.DataRequirement | None = None
        """ Specified value if missing from instance.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate: fhirdate.FHIRDate | None = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Specified value if missing from instance.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.defaultValueDecimal: float | None = None
        """ Specified value if missing from instance.
        Type `float`. """
        
        self.defaultValueDistance: distance.Distance | None = None
        """ Specified value if missing from instance.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage: dosage.Dosage | None = None
        """ Specified value if missing from instance.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration: duration.Duration | None = None
        """ Specified value if missing from instance.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression: expression.Expression | None = None
        """ Specified value if missing from instance.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName: humanname.HumanName | None = None
        """ Specified value if missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueIdentifier: identifier.Identifier | None = None
        """ Specified value if missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant: fhirinstant.FHIRInstant | None = None
        """ Specified value if missing from instance.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.defaultValueInteger: int | None = None
        """ Specified value if missing from instance.
        Type `int`. """
        
        self.defaultValueMarkdown: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueMeta: meta.Meta | None = None
        """ Specified value if missing from instance.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.defaultValueMoney: money.Money | None = None
        """ Specified value if missing from instance.
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Specified value if missing from instance.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod: period.Period | None = None
        """ Specified value if missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt: int | None = None
        """ Specified value if missing from instance.
        Type `int`. """
        
        self.defaultValueQuantity: quantity.Quantity | None = None
        """ Specified value if missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange: range.Range | None = None
        """ Specified value if missing from instance.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio: ratio.Ratio | None = None
        """ Specified value if missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference: fhirreference.FHIRReference | None = None
        """ Specified value if missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Specified value if missing from instance.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData: sampleddata.SampledData | None = None
        """ Specified value if missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature: signature.Signature | None = None
        """ Specified value if missing from instance.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueTime: fhirtime.FHIRTime | None = None
        """ Specified value if missing from instance.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.defaultValueTiming: timing.Timing | None = None
        """ Specified value if missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Specified value if missing from instance.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt: int | None = None
        """ Specified value if missing from instance.
        Type `int`. """
        
        self.defaultValueUri: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueUrl: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.defaultValueUsageContext: usagecontext.UsageContext | None = None
        """ Specified value if missing from instance.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid: str | None = None
        """ Specified value if missing from instance.
        Type `str`. """
        
        self.definition: str | None = None
        """ Full formal definition as narrative text.
        Type `str`. """
        
        self.example: list[ElementDefinitionExample] | None = None
        """ Example value (as defined for type).
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """
        
        self.fixedAddress: address.Address | None = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAge: age.Age | None = None
        """ Value must be exactly this.
        Type `Age` (represented as `dict` in JSON). """
        
        self.fixedAnnotation: annotation.Annotation | None = None
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.fixedAttachment: attachment.Attachment | None = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedBase64Binary: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedBoolean: bool | None = None
        """ Value must be exactly this.
        Type `bool`. """
        
        self.fixedCanonical: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedCode: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fixedCoding: coding.Coding | None = None
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fixedContactDetail: contactdetail.ContactDetail | None = None
        """ Value must be exactly this.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.fixedContactPoint: contactpoint.ContactPoint | None = None
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.fixedContributor: contributor.Contributor | None = None
        """ Value must be exactly this.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.fixedCount: count.Count | None = None
        """ Value must be exactly this.
        Type `Count` (represented as `dict` in JSON). """
        
        self.fixedDataRequirement: datarequirement.DataRequirement | None = None
        """ Value must be exactly this.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.fixedDate: fhirdate.FHIRDate | None = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Value must be exactly this.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.fixedDecimal: float | None = None
        """ Value must be exactly this.
        Type `float`. """
        
        self.fixedDistance: distance.Distance | None = None
        """ Value must be exactly this.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.fixedDosage: dosage.Dosage | None = None
        """ Value must be exactly this.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.fixedDuration: duration.Duration | None = None
        """ Value must be exactly this.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fixedExpression: expression.Expression | None = None
        """ Value must be exactly this.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.fixedHumanName: humanname.HumanName | None = None
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.fixedId: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedIdentifier: identifier.Identifier | None = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedInstant: fhirinstant.FHIRInstant | None = None
        """ Value must be exactly this.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.fixedInteger: int | None = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedMarkdown: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedMeta: meta.Meta | None = None
        """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.fixedMoney: money.Money | None = None
        """ Value must be exactly this.
        Type `Money` (represented as `dict` in JSON). """
        
        self.fixedOid: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Value must be exactly this.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.fixedPeriod: period.Period | None = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        
        self.fixedPositiveInt: int | None = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedQuantity: quantity.Quantity | None = None
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.fixedRange: range.Range | None = None
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """
        
        self.fixedRatio: ratio.Ratio | None = None
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.fixedReference: fhirreference.FHIRReference | None = None
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fixedRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Value must be exactly this.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.fixedSampledData: sampleddata.SampledData | None = None
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.fixedSignature: signature.Signature | None = None
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.fixedString: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedTime: fhirtime.FHIRTime | None = None
        """ Value must be exactly this.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.fixedTiming: timing.Timing | None = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Value must be exactly this.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.fixedUnsignedInt: int | None = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedUri: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedUrl: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedUsageContext: usagecontext.UsageContext | None = None
        """ Value must be exactly this.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.fixedUuid: str | None = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.isModifier: bool | None = None
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self.isModifierReason: str | None = None
        """ Reason that this element is marked as a modifier.
        Type `str`. """
        
        self.isSummary: bool | None = None
        """ Include when _summary = true?.
        Type `bool`. """
        
        self.label: str | None = None
        """ Name for element to display with or prompt for element.
        Type `str`. """
        
        self.mapping: list[ElementDefinitionMapping] | None = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.max: str | None = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.maxLength: int | None = None
        """ Max length for strings.
        Type `int`. """
        
        self.maxValueDate: fhirdate.FHIRDate | None = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.maxValueDecimal: float | None = None
        """ Maximum Allowed Value (for some types).
        Type `float`. """
        
        self.maxValueInstant: fhirinstant.FHIRInstant | None = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.maxValueInteger: int | None = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValuePositiveInt: int | None = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValueQuantity: quantity.Quantity | None = None
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxValueTime: fhirtime.FHIRTime | None = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.maxValueUnsignedInt: int | None = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.meaningWhenMissing: str | None = None
        """ Implicit meaning when this element is missing.
        Type `str`. """
        
        self.min: int | None = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.minValueDate: fhirdate.FHIRDate | None = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.minValueDecimal: float | None = None
        """ Minimum Allowed Value (for some types).
        Type `float`. """
        
        self.minValueInstant: fhirinstant.FHIRInstant | None = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.minValueInteger: int | None = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValuePositiveInt: int | None = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValueQuantity: quantity.Quantity | None = None
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minValueTime: fhirtime.FHIRTime | None = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.minValueUnsignedInt: int | None = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.mustSupport: bool | None = None
        """ If the element must be supported.
        Type `bool`. """
        
        self.orderMeaning: str | None = None
        """ What the order of the elements means.
        Type `str`. """
        
        self.path: str | None = None
        """ Path of the element in the hierarchy of elements.
        Type `str`. """
        
        self.patternAddress: address.Address | None = None
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """
        
        self.patternAge: age.Age | None = None
        """ Value must have at least these property values.
        Type `Age` (represented as `dict` in JSON). """
        
        self.patternAnnotation: annotation.Annotation | None = None
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patternAttachment: attachment.Attachment | None = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternBase64Binary: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternBoolean: bool | None = None
        """ Value must have at least these property values.
        Type `bool`. """
        
        self.patternCanonical: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternCode: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patternCoding: coding.Coding | None = None
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patternContactDetail: contactdetail.ContactDetail | None = None
        """ Value must have at least these property values.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.patternContactPoint: contactpoint.ContactPoint | None = None
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.patternContributor: contributor.Contributor | None = None
        """ Value must have at least these property values.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.patternCount: count.Count | None = None
        """ Value must have at least these property values.
        Type `Count` (represented as `dict` in JSON). """
        
        self.patternDataRequirement: datarequirement.DataRequirement | None = None
        """ Value must have at least these property values.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.patternDate: fhirdate.FHIRDate | None = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Value must have at least these property values.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.patternDecimal: float | None = None
        """ Value must have at least these property values.
        Type `float`. """
        
        self.patternDistance: distance.Distance | None = None
        """ Value must have at least these property values.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.patternDosage: dosage.Dosage | None = None
        """ Value must have at least these property values.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.patternDuration: duration.Duration | None = None
        """ Value must have at least these property values.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.patternExpression: expression.Expression | None = None
        """ Value must have at least these property values.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.patternHumanName: humanname.HumanName | None = None
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patternId: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternIdentifier: identifier.Identifier | None = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternInstant: fhirinstant.FHIRInstant | None = None
        """ Value must have at least these property values.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.patternInteger: int | None = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternMarkdown: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternMeta: meta.Meta | None = None
        """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.patternMoney: money.Money | None = None
        """ Value must have at least these property values.
        Type `Money` (represented as `dict` in JSON). """
        
        self.patternOid: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Value must have at least these property values.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.patternPeriod: period.Period | None = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        
        self.patternPositiveInt: int | None = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternQuantity: quantity.Quantity | None = None
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.patternRange: range.Range | None = None
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """
        
        self.patternRatio: ratio.Ratio | None = None
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.patternReference: fhirreference.FHIRReference | None = None
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patternRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Value must have at least these property values.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.patternSampledData: sampleddata.SampledData | None = None
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.patternSignature: signature.Signature | None = None
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.patternString: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternTime: fhirtime.FHIRTime | None = None
        """ Value must have at least these property values.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.patternTiming: timing.Timing | None = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.patternTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Value must have at least these property values.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.patternUnsignedInt: int | None = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternUri: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternUrl: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternUsageContext: usagecontext.UsageContext | None = None
        """ Value must have at least these property values.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.patternUuid: str | None = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.representation: list[str | None] | None = None
        """ xmlAttr | xmlText | typeAttr | cdaText | xhtml.
        List of `str` items. """
        
        self.requirements: str | None = None
        """ Why this resource has been created.
        Type `str`. """
        
        self.short: str | None = None
        """ Concise definition for space-constrained presentation.
        Type `str`. """
        
        self.sliceIsConstraining: bool | None = None
        """ If this slice definition constrains an inherited slice definition
        (or not).
        Type `bool`. """
        
        self.sliceName: str | None = None
        """ Name for this particular element (in a set of slices).
        Type `str`. """
        
        self.slicing: ElementDefinitionSlicing | None = None
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        
        self.type: list[ElementDefinitionType] | None = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdatetime.FHIRDateTime, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirinstant.FHIRInstant, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirtime.FHIRTime, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("definition", "definition", str, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False),
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", fhirdatetime.FHIRDateTime, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False),
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False),
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False),
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", fhirinstant.FHIRInstant, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedMeta", "fixedMeta", meta.Meta, False, "fixed", False),
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", fhirtime.FHIRTime, False, "fixed", False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("maxValueDate", "maxValueDate", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", fhirdatetime.FHIRDateTime, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", fhirinstant.FHIRInstant, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", fhirtime.FHIRTime, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("minValueDate", "minValueDate", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", fhirdatetime.FHIRDateTime, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueInstant", "minValueInstant", fhirinstant.FHIRInstant, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("minValueTime", "minValueTime", fhirtime.FHIRTime, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("path", "path", str, False, None, True),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("patternAge", "patternAge", age.Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False),
            ("patternCount", "patternCount", count.Count, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", fhirdatetime.FHIRDateTime, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False),
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False),
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False),
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", fhirinstant.FHIRInstant, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternMeta", "patternMeta", meta.Meta, False, "pattern", False),
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", fhirtime.FHIRTime, False, "pattern", False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("representation", "representation", str, True, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("short", "short", str, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
        ])
        return js


from . import element

class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    
    resource_type = "ElementDefinitionBase"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.max: str | None = None
        """ Max cardinality of the base element.
        Type `str`. """
        
        self.min: int | None = None
        """ Min cardinality of the base element.
        Type `int`. """
        
        self.path: str | None = None
        """ Path that identifies the base element.
        Type `str`. """
        
        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    
    resource_type = "ElementDefinitionBinding"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.strength: str | None = None
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self.valueSet: str | None = None
        """ Source of value set.
        Type `str`. """
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    resource_type = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression: str | None = None
        """ FHIRPath expression of constraint.
        Type `str`. """
        
        self.human: str | None = None
        """ Human description of constraint.
        Type `str`. """
        
        self.key: str | None = None
        """ Target of 'condition' reference above.
        Type `str`. """
        
        self.requirements: str | None = None
        """ Why this constraint is necessary or appropriate.
        Type `str`. """
        
        self.severity: str | None = None
        """ error | warning.
        Type `str`. """
        
        self.source: str | None = None
        """ Reference to original source of constraint.
        Type `str`. """
        
        self.xpath: str | None = None
        """ XPath expression of constraint.
        Type `str`. """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, False),
            ("human", "human", str, False, None, True),
            ("key", "key", str, False, None, True),
            ("requirements", "requirements", str, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("source", "source", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
        ])
        return js


class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).
    
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    
    resource_type = "ElementDefinitionExample"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label: str | None = None
        """ Describes the purpose of this example.
        Type `str`. """
        
        self.valueAddress: address.Address | None = None
        """ Value of Example (one of allowed types).
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge: age.Age | None = None
        """ Value of Example (one of allowed types).
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation: annotation.Annotation | None = None
        """ Value of Example (one of allowed types).
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment: attachment.Attachment | None = None
        """ Value of Example (one of allowed types).
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueBoolean: bool | None = None
        """ Value of Example (one of allowed types).
        Type `bool`. """
        
        self.valueCanonical: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueCode: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Value of Example (one of allowed types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding: coding.Coding | None = None
        """ Value of Example (one of allowed types).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail: contactdetail.ContactDetail | None = None
        """ Value of Example (one of allowed types).
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint: contactpoint.ContactPoint | None = None
        """ Value of Example (one of allowed types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor: contributor.Contributor | None = None
        """ Value of Example (one of allowed types).
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount: count.Count | None = None
        """ Value of Example (one of allowed types).
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement: datarequirement.DataRequirement | None = None
        """ Value of Example (one of allowed types).
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate: fhirdate.FHIRDate | None = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Value of Example (one of allowed types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal: float | None = None
        """ Value of Example (one of allowed types).
        Type `float`. """
        
        self.valueDistance: distance.Distance | None = None
        """ Value of Example (one of allowed types).
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage: dosage.Dosage | None = None
        """ Value of Example (one of allowed types).
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration: duration.Duration | None = None
        """ Value of Example (one of allowed types).
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression: expression.Expression | None = None
        """ Value of Example (one of allowed types).
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName: humanname.HumanName | None = None
        """ Value of Example (one of allowed types).
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueIdentifier: identifier.Identifier | None = None
        """ Value of Example (one of allowed types).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant: fhirinstant.FHIRInstant | None = None
        """ Value of Example (one of allowed types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger: int | None = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self.valueMarkdown: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueMeta: meta.Meta | None = None
        """ Value of Example (one of allowed types).
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney: money.Money | None = None
        """ Value of Example (one of allowed types).
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Value of Example (one of allowed types).
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod: period.Period | None = None
        """ Value of Example (one of allowed types).
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt: int | None = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self.valueQuantity: quantity.Quantity | None = None
        """ Value of Example (one of allowed types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange: range.Range | None = None
        """ Value of Example (one of allowed types).
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio: ratio.Ratio | None = None
        """ Value of Example (one of allowed types).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference: fhirreference.FHIRReference | None = None
        """ Value of Example (one of allowed types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Value of Example (one of allowed types).
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData: sampleddata.SampledData | None = None
        """ Value of Example (one of allowed types).
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature: signature.Signature | None = None
        """ Value of Example (one of allowed types).
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueTime: fhirtime.FHIRTime | None = None
        """ Value of Example (one of allowed types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueTiming: timing.Timing | None = None
        """ Value of Example (one of allowed types).
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Value of Example (one of allowed types).
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt: int | None = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self.valueUri: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueUrl: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        self.valueUsageContext: usagecontext.UsageContext | None = None
        """ Value of Example (one of allowed types).
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid: str | None = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        
        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
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


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_type = "ElementDefinitionMapping"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment: str | None = None
        """ Comments about the mapping or its use.
        Type `str`. """
        
        self.identity: str | None = None
        """ Reference to mapping declaration.
        Type `str`. """
        
        self.language: str | None = None
        """ Computable language of mapping.
        Type `str`. """
        
        self.map: str | None = None
        """ Details of the mapping.
        Type `str`. """
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("language", "language", str, False, None, False),
            ("map", "map", str, False, None, True),
        ])
        return js


class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    
    resource_type = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Text description of how slicing works (or not).
        Type `str`. """
        
        self.discriminator: list[ElementDefinitionSlicingDiscriminator] | None = None
        """ Element values that are used to distinguish the slices.
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """
        
        self.ordered: bool | None = None
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules: str | None = None
        """ closed | open | openAtEnd.
        Type `str`. """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("rules", "rules", str, False, None, True),
        ])
        return js


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.
    
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    
    resource_type = "ElementDefinitionSlicingDiscriminator"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path: str | None = None
        """ Path to element value.
        Type `str`. """
        
        self.type: str | None = None
        """ value | exists | pattern | type | profile.
        Type `str`. """
        
        super(ElementDefinitionSlicingDiscriminator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    resource_type = "ElementDefinitionType"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.aggregation: list[str | None] | None = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        
        self.code: str | None = None
        """ Data type or Resource (reference to definition).
        Type `str`. """
        
        self.profile: list[str | None] | None = None
        """ Profiles (StructureDefinition or IG) - one must apply.
        List of `str` items. """
        
        self.targetProfile: list[str | None] | None = None
        """ Profile (StructureDefinition or IG) on the Reference/canonical
        target - one must apply.
        List of `str` items. """
        
        self.versioning: str | None = None
        """ either | independent | specific.
        Type `str`. """
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("profile", "profile", str, True, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("versioning", "versioning", str, False, None, False),
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
