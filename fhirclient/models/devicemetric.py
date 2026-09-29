# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceMetric).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_type = "DeviceMetric"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.calibration: list[DeviceMetricCalibration] | None = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        self.category: str | None = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """
        
        self.color: str | None = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """
        
        self.identifier: list[identifier.Identifier] | None = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.measurementPeriod: timing.Timing | None = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.operationalStatus: str | None = None
        """ on | off | standby | entered-in-error.
        Type `str`. """
        
        self.parent: fhirreference.FHIRReference | None = None
        """ Describes the link to the parent Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source: fhirreference.FHIRReference | None = None
        """ Describes the link to the source Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type: codeableconcept.CodeableConcept | None = None
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit: codeableconcept.CodeableConcept | None = None
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
            ("category", "category", str, False, None, True),
            ("color", "color", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    resource_type = "DeviceMetricCalibration"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.state: str | None = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """
        
        self.time: fhirinstant.FHIRInstant | None = None
        """ Describes the time last calibration has been performed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.type: str | None = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """
        
        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False, None, False),
            ("time", "time", fhirinstant.FHIRInstant, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import timing
