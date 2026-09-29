# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MolecularSequence).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class MolecularSequence(domainresource.DomainResource):
    """ Information about a biological sequence.
    
    Raw data describing a biological sequence.
    """
    
    resource_type = "MolecularSequence"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coordinateSystem: int | None = None
        """ Base number of coordinate system (0 for 0-based numbering or
        coordinates, inclusive start, exclusive end, 1 for 1-based
        numbering, inclusive start, inclusive end).
        Type `int`. """
        
        self.device: fhirreference.FHIRReference | None = None
        """ The method for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Unique ID for this particular sequence. This is a FHIR-defined id.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.observedSeq: str | None = None
        """ Sequence that was observed.
        Type `str`. """
        
        self.patient: fhirreference.FHIRReference | None = None
        """ Who and/or what this is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer: fhirreference.FHIRReference | None = None
        """ Who should be responsible for test result.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.pointer: list[fhirreference.FHIRReference] | None = None
        """ Pointer to next atomic sequence.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.quality: list[MolecularSequenceQuality] | None = None
        """ An set of value as quality of sequence.
        List of `MolecularSequenceQuality` items (represented as `dict` in JSON). """
        
        self.quantity: quantity.Quantity | None = None
        """ The number of copies of the sequence of interest.  (RNASeq).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.readCoverage: int | None = None
        """ Average number of reads representing a given nucleotide in the
        reconstructed sequence.
        Type `int`. """
        
        self.referenceSeq: MolecularSequenceReferenceSeq | None = None
        """ A sequence used as reference.
        Type `MolecularSequenceReferenceSeq` (represented as `dict` in JSON). """
        
        self.repository: list[MolecularSequenceRepository] | None = None
        """ External repository which contains detailed report related with
        observedSeq in this resource.
        List of `MolecularSequenceRepository` items (represented as `dict` in JSON). """
        
        self.specimen: fhirreference.FHIRReference | None = None
        """ Specimen used for sequencing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.structureVariant: list[MolecularSequenceStructureVariant] | None = None
        """ Structural variant.
        List of `MolecularSequenceStructureVariant` items (represented as `dict` in JSON). """
        
        self.type: str | None = None
        """ aa | dna | rna.
        Type `str`. """
        
        self.variant: list[MolecularSequenceVariant] | None = None
        """ Variant in sequence.
        List of `MolecularSequenceVariant` items (represented as `dict` in JSON). """
        
        super(MolecularSequence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequence, self).elementProperties()
        js.extend([
            ("coordinateSystem", "coordinateSystem", int, False, None, True),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("observedSeq", "observedSeq", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("pointer", "pointer", fhirreference.FHIRReference, True, None, False),
            ("quality", "quality", MolecularSequenceQuality, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("readCoverage", "readCoverage", int, False, None, False),
            ("referenceSeq", "referenceSeq", MolecularSequenceReferenceSeq, False, None, False),
            ("repository", "repository", MolecularSequenceRepository, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("structureVariant", "structureVariant", MolecularSequenceStructureVariant, True, None, False),
            ("type", "type", str, False, None, False),
            ("variant", "variant", MolecularSequenceVariant, True, None, False),
        ])
        return js


from . import backboneelement

class MolecularSequenceQuality(backboneelement.BackboneElement):
    """ An set of value as quality of sequence.
    
    An experimental feature attribute that defines the quality of the feature
    in a quantitative way, such as a phred quality score ([SO:0001686](http://w
    ww.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    """
    
    resource_type = "MolecularSequenceQuality"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end: int | None = None
        """ End position of the sequence.
        Type `int`. """
        
        self.fScore: float | None = None
        """ F-score.
        Type `float`. """
        
        self.gtFP: float | None = None
        """ False positives where the non-REF alleles in the Truth and Query
        Call Sets match.
        Type `float`. """
        
        self.method: codeableconcept.CodeableConcept | None = None
        """ Method to get quality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.precision: float | None = None
        """ Precision of comparison.
        Type `float`. """
        
        self.queryFP: float | None = None
        """ False positives.
        Type `float`. """
        
        self.queryTP: float | None = None
        """ True positives from the perspective of the query data.
        Type `float`. """
        
        self.recall: float | None = None
        """ Recall of comparison.
        Type `float`. """
        
        self.roc: MolecularSequenceQualityRoc | None = None
        """ Receiver Operator Characteristic (ROC) Curve.
        Type `MolecularSequenceQualityRoc` (represented as `dict` in JSON). """
        
        self.score: quantity.Quantity | None = None
        """ Quality score for the comparison.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.standardSequence: codeableconcept.CodeableConcept | None = None
        """ Standard sequence for comparison.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start: int | None = None
        """ Start position of the sequence.
        Type `int`. """
        
        self.truthFN: float | None = None
        """ False negatives.
        Type `float`. """
        
        self.truthTP: float | None = None
        """ True positives from the perspective of the truth data.
        Type `float`. """
        
        self.type: str | None = None
        """ indel | snp | unknown.
        Type `str`. """
        
        super(MolecularSequenceQuality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceQuality, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("fScore", "fScore", float, False, None, False),
            ("gtFP", "gtFP", float, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("precision", "precision", float, False, None, False),
            ("queryFP", "queryFP", float, False, None, False),
            ("queryTP", "queryTP", float, False, None, False),
            ("recall", "recall", float, False, None, False),
            ("roc", "roc", MolecularSequenceQualityRoc, False, None, False),
            ("score", "score", quantity.Quantity, False, None, False),
            ("standardSequence", "standardSequence", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", int, False, None, False),
            ("truthFN", "truthFN", float, False, None, False),
            ("truthTP", "truthTP", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    """ Receiver Operator Characteristic (ROC) Curve.
    
    Receiver Operator Characteristic (ROC) Curve  to give
    sensitivity/specificity tradeoff.
    """
    
    resource_type = "MolecularSequenceQualityRoc"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fMeasure: list[float | None] | None = None
        """ FScore of the GQ score.
        List of `float` items. """
        
        self.numFN: list[int | None] | None = None
        """ Roc score false negative numbers.
        List of `int` items. """
        
        self.numFP: list[int | None] | None = None
        """ Roc score false positive numbers.
        List of `int` items. """
        
        self.numTP: list[int | None] | None = None
        """ Roc score true positive numbers.
        List of `int` items. """
        
        self.precision: list[float | None] | None = None
        """ Precision of the GQ score.
        List of `float` items. """
        
        self.score: list[int | None] | None = None
        """ Genotype quality score.
        List of `int` items. """
        
        self.sensitivity: list[float | None] | None = None
        """ Sensitivity of the GQ score.
        List of `float` items. """
        
        super(MolecularSequenceQualityRoc, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceQualityRoc, self).elementProperties()
        js.extend([
            ("fMeasure", "fMeasure", float, True, None, False),
            ("numFN", "numFN", int, True, None, False),
            ("numFP", "numFP", int, True, None, False),
            ("numTP", "numTP", int, True, None, False),
            ("precision", "precision", float, True, None, False),
            ("score", "score", int, True, None, False),
            ("sensitivity", "sensitivity", float, True, None, False),
        ])
        return js


class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    """ A sequence used as reference.
    
    A sequence that is used as a reference to describe variants that are
    present in a sequence analyzed.
    """
    
    resource_type = "MolecularSequenceReferenceSeq"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chromosome: codeableconcept.CodeableConcept | None = None
        """ Chromosome containing genetic finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genomeBuild: str | None = None
        """ The Genome Build used for reference, following GRCh build versions
        e.g. 'GRCh 37'.
        Type `str`. """
        
        self.orientation: str | None = None
        """ sense | antisense.
        Type `str`. """
        
        self.referenceSeqId: codeableconcept.CodeableConcept | None = None
        """ Reference identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referenceSeqPointer: fhirreference.FHIRReference | None = None
        """ A pointer to another MolecularSequence entity as reference sequence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceSeqString: str | None = None
        """ A string to represent reference sequence.
        Type `str`. """
        
        self.strand: str | None = None
        """ watson | crick.
        Type `str`. """
        
        self.windowEnd: int | None = None
        """ End position of the window on the reference sequence.
        Type `int`. """
        
        self.windowStart: int | None = None
        """ Start position of the window on the  reference sequence.
        Type `int`. """
        
        super(MolecularSequenceReferenceSeq, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceReferenceSeq, self).elementProperties()
        js.extend([
            ("chromosome", "chromosome", codeableconcept.CodeableConcept, False, None, False),
            ("genomeBuild", "genomeBuild", str, False, None, False),
            ("orientation", "orientation", str, False, None, False),
            ("referenceSeqId", "referenceSeqId", codeableconcept.CodeableConcept, False, None, False),
            ("referenceSeqPointer", "referenceSeqPointer", fhirreference.FHIRReference, False, None, False),
            ("referenceSeqString", "referenceSeqString", str, False, None, False),
            ("strand", "strand", str, False, None, False),
            ("windowEnd", "windowEnd", int, False, None, False),
            ("windowStart", "windowStart", int, False, None, False),
        ])
        return js


class MolecularSequenceRepository(backboneelement.BackboneElement):
    """ External repository which contains detailed report related with observedSeq
    in this resource.
    
    Configurations of the external repository. The repository shall store
    target's observedSeq or records related with target's observedSeq.
    """
    
    resource_type = "MolecularSequenceRepository"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.datasetId: str | None = None
        """ Id of the dataset that used to call for dataset in repository.
        Type `str`. """
        
        self.name: str | None = None
        """ Repository's name.
        Type `str`. """
        
        self.readsetId: str | None = None
        """ Id of the read.
        Type `str`. """
        
        self.type: str | None = None
        """ directlink | openapi | login | oauth | other.
        Type `str`. """
        
        self.url: str | None = None
        """ URI of the repository.
        Type `str`. """
        
        self.variantsetId: str | None = None
        """ Id of the variantset that used to call for variantset in repository.
        Type `str`. """
        
        super(MolecularSequenceRepository, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceRepository, self).elementProperties()
        js.extend([
            ("datasetId", "datasetId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("readsetId", "readsetId", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("variantsetId", "variantsetId", str, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    """ Structural variant.
    
    Information about chromosome structure variation.
    """
    
    resource_type = "MolecularSequenceStructureVariant"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exact: bool | None = None
        """ Does the structural variant have base pair resolution breakpoints?.
        Type `bool`. """
        
        self.inner: MolecularSequenceStructureVariantInner | None = None
        """ Structural variant inner.
        Type `MolecularSequenceStructureVariantInner` (represented as `dict` in JSON). """
        
        self.length: int | None = None
        """ Structural variant length.
        Type `int`. """
        
        self.outer: MolecularSequenceStructureVariantOuter | None = None
        """ Structural variant outer.
        Type `MolecularSequenceStructureVariantOuter` (represented as `dict` in JSON). """
        
        self.variantType: codeableconcept.CodeableConcept | None = None
        """ Structural variant change type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MolecularSequenceStructureVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceStructureVariant, self).elementProperties()
        js.extend([
            ("exact", "exact", bool, False, None, False),
            ("inner", "inner", MolecularSequenceStructureVariantInner, False, None, False),
            ("length", "length", int, False, None, False),
            ("outer", "outer", MolecularSequenceStructureVariantOuter, False, None, False),
            ("variantType", "variantType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    """ Structural variant inner.
    """
    
    resource_type = "MolecularSequenceStructureVariantInner"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end: int | None = None
        """ Structural variant inner end.
        Type `int`. """
        
        self.start: int | None = None
        """ Structural variant inner start.
        Type `int`. """
        
        super(MolecularSequenceStructureVariantInner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceStructureVariantInner, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    """ Structural variant outer.
    """
    
    resource_type = "MolecularSequenceStructureVariantOuter"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end: int | None = None
        """ Structural variant outer end.
        Type `int`. """
        
        self.start: int | None = None
        """ Structural variant outer start.
        Type `int`. """
        
        super(MolecularSequenceStructureVariantOuter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceStructureVariantOuter, self).elementProperties()
        js.extend([
            ("end", "end", int, False, None, False),
            ("start", "start", int, False, None, False),
        ])
        return js


class MolecularSequenceVariant(backboneelement.BackboneElement):
    """ Variant in sequence.
    
    The definition of variant here originates from Sequence ontology ([variant_
    of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)).
    This element can represent amino acid or nucleic sequence change(including
    insertion,deletion,SNP,etc.)  It can represent some complex mutation or
    segment variation with the assist of CIGAR string.
    """
    
    resource_type = "MolecularSequenceVariant"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cigar: str | None = None
        """ Extended CIGAR string for aligning the sequence with reference
        bases.
        Type `str`. """
        
        self.end: int | None = None
        """ End position of the variant on the reference sequence.
        Type `int`. """
        
        self.observedAllele: str | None = None
        """ Allele that was observed.
        Type `str`. """
        
        self.referenceAllele: str | None = None
        """ Allele in the reference sequence.
        Type `str`. """
        
        self.start: int | None = None
        """ Start position of the variant on the  reference sequence.
        Type `int`. """
        
        self.variantPointer: fhirreference.FHIRReference | None = None
        """ Pointer to observed variant information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MolecularSequenceVariant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(MolecularSequenceVariant, self).elementProperties()
        js.extend([
            ("cigar", "cigar", str, False, None, False),
            ("end", "end", int, False, None, False),
            ("observedAllele", "observedAllele", str, False, None, False),
            ("referenceAllele", "referenceAllele", str, False, None, False),
            ("start", "start", int, False, None, False),
            ("variantPointer", "variantPointer", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import quantity
