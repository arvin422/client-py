# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureMap).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class StructureMap(domainresource.DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform
    data.
    """
    
    resource_type = "StructureMap"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact: list[contactdetail.ContactDetail] | None = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright: str | None = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date: fhirdatetime.FHIRDateTime | None = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description: str | None = None
        """ Natural language description of the structure map.
        Type `str`. """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.group: list[StructureMapGroup] | None = None
        """ Named sections for reader convenience.
        List of `StructureMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Additional identifier for the structure map.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.import_fhir: list[str | None] | None = None
        """ Other maps used by this map (canonical URLs).
        List of `str` items. """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for structure map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Name for this structure map (computer friendly).
        Type `str`. """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose: str | None = None
        """ Why this structure map is defined.
        Type `str`. """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.structure: list[StructureMapStructure] | None = None
        """ Structure Definition used by this map.
        List of `StructureMapStructure` items (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Name for this structure map (human friendly).
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical identifier for this structure map, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the structure map.
        Type `str`. """
        
        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class StructureMapGroup(backboneelement.BackboneElement):
    """ Named sections for reader convenience.
    
    Organizes the mapping into manageable chunks for human review/ease of
    maintenance.
    """
    
    resource_type = "StructureMapGroup"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation: str | None = None
        """ Additional description/explanation for group.
        Type `str`. """
        
        self.extends: str | None = None
        """ Another group that this group adds rules to.
        Type `str`. """
        
        self.input: list[StructureMapGroupInput] | None = None
        """ Named instance provided when invoking the map.
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Human-readable label.
        Type `str`. """
        
        self.rule: list[StructureMapGroupRule] | None = None
        """ Transform Rule from source to target.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.typeMode: str | None = None
        """ none | types | type-and-types.
        Type `str`. """
        
        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("typeMode", "typeMode", str, False, None, True),
        ])
        return js


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ Named instance provided when invoking the map.
    
    A name assigned to an instance of data. The instance must be provided when
    the mapping is invoked.
    """
    
    resource_type = "StructureMapGroupInput"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation: str | None = None
        """ Documentation for this instance of data.
        Type `str`. """
        
        self.mode: str | None = None
        """ source | target.
        Type `str`. """
        
        self.name: str | None = None
        """ Name for this instance of data.
        Type `str`. """
        
        self.type: str | None = None
        """ Type for this instance of data.
        Type `str`. """
        
        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ Transform Rule from source to target.
    """
    
    resource_type = "StructureMapGroupRule"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dependent: list[StructureMapGroupRuleDependent] | None = None
        """ Which other rules to apply in the context of this rule.
        List of `StructureMapGroupRuleDependent` items (represented as `dict` in JSON). """
        
        self.documentation: str | None = None
        """ Documentation for this instance of data.
        Type `str`. """
        
        self.name: str | None = None
        """ Name of the rule for internal references.
        Type `str`. """
        
        self.rule: list[StructureMapGroupRule] | None = None
        """ Rules contained in this rule.
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.source: list[StructureMapGroupRuleSource] | None = None
        """ Source inputs to the mapping.
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """
        
        self.target: list[StructureMapGroupRuleTarget] | None = None
        """ Content to create because of this mapping rule.
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """
        
        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
        ])
        return js


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ Which other rules to apply in the context of this rule.
    """
    
    resource_type = "StructureMapGroupRuleDependent"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name: str | None = None
        """ Name of a rule or group to apply.
        Type `str`. """
        
        self.variable: list[str | None] | None = None
        """ Variable to pass to the rule or group.
        List of `str` items. """
        
        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("variable", "variable", str, True, None, True),
        ])
        return js


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ Source inputs to the mapping.
    """
    
    resource_type = "StructureMapGroupRuleSource"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.check: str | None = None
        """ FHIRPath expression  - must be true or the mapping engine throws an
        error instead of completing.
        Type `str`. """
        
        self.condition: str | None = None
        """ FHIRPath expression  - must be true or the rule does not apply.
        Type `str`. """
        
        self.context: str | None = None
        """ Type or variable this rule applies to.
        Type `str`. """
        
        self.defaultValueAddress: address.Address | None = None
        """ Default value if no value exists.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge: age.Age | None = None
        """ Default value if no value exists.
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation: annotation.Annotation | None = None
        """ Default value if no value exists.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment: attachment.Attachment | None = None
        """ Default value if no value exists.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueBoolean: bool | None = None
        """ Default value if no value exists.
        Type `bool`. """
        
        self.defaultValueCanonical: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueCode: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueCodeableConcept: codeableconcept.CodeableConcept | None = None
        """ Default value if no value exists.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding: coding.Coding | None = None
        """ Default value if no value exists.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail: contactdetail.ContactDetail | None = None
        """ Default value if no value exists.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint: contactpoint.ContactPoint | None = None
        """ Default value if no value exists.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor: contributor.Contributor | None = None
        """ Default value if no value exists.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount: count.Count | None = None
        """ Default value if no value exists.
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement: datarequirement.DataRequirement | None = None
        """ Default value if no value exists.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate: fhirdate.FHIRDate | None = None
        """ Default value if no value exists.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime: fhirdatetime.FHIRDateTime | None = None
        """ Default value if no value exists.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.defaultValueDecimal: float | None = None
        """ Default value if no value exists.
        Type `float`. """
        
        self.defaultValueDistance: distance.Distance | None = None
        """ Default value if no value exists.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage: dosage.Dosage | None = None
        """ Default value if no value exists.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration: duration.Duration | None = None
        """ Default value if no value exists.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression: expression.Expression | None = None
        """ Default value if no value exists.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName: humanname.HumanName | None = None
        """ Default value if no value exists.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueIdentifier: identifier.Identifier | None = None
        """ Default value if no value exists.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant: fhirinstant.FHIRInstant | None = None
        """ Default value if no value exists.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.defaultValueInteger: int | None = None
        """ Default value if no value exists.
        Type `int`. """
        
        self.defaultValueMarkdown: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueMeta: meta.Meta | None = None
        """ Default value if no value exists.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.defaultValueMoney: money.Money | None = None
        """ Default value if no value exists.
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueParameterDefinition: parameterdefinition.ParameterDefinition | None = None
        """ Default value if no value exists.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod: period.Period | None = None
        """ Default value if no value exists.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt: int | None = None
        """ Default value if no value exists.
        Type `int`. """
        
        self.defaultValueQuantity: quantity.Quantity | None = None
        """ Default value if no value exists.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange: range.Range | None = None
        """ Default value if no value exists.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio: ratio.Ratio | None = None
        """ Default value if no value exists.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference: fhirreference.FHIRReference | None = None
        """ Default value if no value exists.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact: relatedartifact.RelatedArtifact | None = None
        """ Default value if no value exists.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData: sampleddata.SampledData | None = None
        """ Default value if no value exists.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature: signature.Signature | None = None
        """ Default value if no value exists.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueTime: fhirtime.FHIRTime | None = None
        """ Default value if no value exists.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.defaultValueTiming: timing.Timing | None = None
        """ Default value if no value exists.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition: triggerdefinition.TriggerDefinition | None = None
        """ Default value if no value exists.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt: int | None = None
        """ Default value if no value exists.
        Type `int`. """
        
        self.defaultValueUri: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueUrl: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.defaultValueUsageContext: usagecontext.UsageContext | None = None
        """ Default value if no value exists.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid: str | None = None
        """ Default value if no value exists.
        Type `str`. """
        
        self.element: str | None = None
        """ Optional field for this source.
        Type `str`. """
        
        self.listMode: str | None = None
        """ first | not_first | last | not_last | only_one.
        Type `str`. """
        
        self.logMessage: str | None = None
        """ Message to put in log if source exists (FHIRPath).
        Type `str`. """
        
        self.max: str | None = None
        """ Specified maximum cardinality (number or *).
        Type `str`. """
        
        self.min: int | None = None
        """ Specified minimum cardinality.
        Type `int`. """
        
        self.type: str | None = None
        """ Rule only applies if source has this type.
        Type `str`. """
        
        self.variable: str | None = None
        """ Named context for field, if a field is specified.
        Type `str`. """
        
        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", str, False, None, True),
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
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ Content to create because of this mapping rule.
    """
    
    resource_type = "StructureMapGroupRuleTarget"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context: str | None = None
        """ Type or variable this rule applies to.
        Type `str`. """
        
        self.contextType: str | None = None
        """ type | variable.
        Type `str`. """
        
        self.element: str | None = None
        """ Field to create in the context.
        Type `str`. """
        
        self.listMode: list[str | None] | None = None
        """ first | share | last | collate.
        List of `str` items. """
        
        self.listRuleId: str | None = None
        """ Internal rule reference for shared list items.
        Type `str`. """
        
        self.parameter: list[StructureMapGroupRuleTargetParameter] | None = None
        """ Parameters to the transform.
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """
        
        self.transform: str | None = None
        """ create | copy +.
        Type `str`. """
        
        self.variable: str | None = None
        """ Named context for field, if desired, and a field is specified.
        Type `str`. """
        
        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ Parameters to the transform.
    """
    
    resource_type = "StructureMapGroupRuleTargetParameter"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean: bool | None = None
        """ Parameter value - variable or literal.
        Type `bool`. """
        
        self.valueDecimal: float | None = None
        """ Parameter value - variable or literal.
        Type `float`. """
        
        self.valueId: str | None = None
        """ Parameter value - variable or literal.
        Type `str`. """
        
        self.valueInteger: int | None = None
        """ Parameter value - variable or literal.
        Type `int`. """
        
        self.valueString: str | None = None
        """ Parameter value - variable or literal.
        Type `str`. """
        
        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


class StructureMapStructure(backboneelement.BackboneElement):
    """ Structure Definition used by this map.
    
    A structure definition used by this map. The structure definition may
    describe instances that are converted, or the instances that are produced.
    """
    
    resource_type = "StructureMapStructure"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias: str | None = None
        """ Name for type in this map.
        Type `str`. """
        
        self.documentation: str | None = None
        """ Documentation on use of structure.
        Type `str`. """
        
        self.mode: str | None = None
        """ source | queried | target | produced.
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical reference to structure definition.
        Type `str`. """
        
        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, True),
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
