# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestReport).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.
    
    A summary of information based on the results of executing a TestScript.
    """
    
    resource_type = "TestReport"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier: identifier.Identifier | None = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued: fhirdatetime.FHIRDateTime | None = None
        """ When the TestScript was executed and this TestReport was generated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.name: str | None = None
        """ Informal name of the executed TestScript.
        Type `str`. """
        
        self.participant: list[TestReportParticipant] | None = None
        """ A participant in the test execution, either the execution engine, a
        client, or a server.
        List of `TestReportParticipant` items (represented as `dict` in JSON). """
        
        self.result: str | None = None
        """ pass | fail | pending.
        Type `str`. """
        
        self.score: float | None = None
        """ The final score (percentage of tests passed) resulting from the
        execution of the TestScript.
        Type `float`. """
        
        self.setup: TestReportSetup | None = None
        """ The results of the series of required setup operations before the
        tests were executed.
        Type `TestReportSetup` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ completed | in-progress | waiting | stopped | entered-in-error.
        Type `str`. """
        
        self.teardown: TestReportTeardown | None = None
        """ The results of running the series of required clean up steps.
        Type `TestReportTeardown` (represented as `dict` in JSON). """
        
        self.test: list[TestReportTest] | None = None
        """ A test executed from the test script.
        List of `TestReportTest` items (represented as `dict` in JSON). """
        
        self.testScript: fhirreference.FHIRReference | None = None
        """ Reference to the  version-specific TestScript that was executed to
        produce this TestReport.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.tester: str | None = None
        """ Name of the tester producing this report (Organization or
        individual).
        Type `str`. """
        
        super(TestReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdatetime.FHIRDateTime, False, None, False),
            ("name", "name", str, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("result", "result", str, False, None, True),
            ("score", "score", float, False, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True),
            ("tester", "tester", str, False, None, False),
        ])
        return js


from . import backboneelement

class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """
    
    resource_type = "TestReportParticipant"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display: str | None = None
        """ The display name of the participant.
        Type `str`. """
        
        self.type: str | None = None
        """ test-engine | client | server.
        Type `str`. """
        
        self.uri: str | None = None
        """ The uri of the participant. An absolute URL is preferred.
        Type `str`. """
        
        super(TestReportParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
        ])
        return js


class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """
    
    resource_type = "TestReportSetup"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestReportSetupAction] | None = None
        """ A setup operation or assert that was executed.
        List of `TestReportSetupAction` items (represented as `dict` in JSON). """
        
        super(TestReportSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
        ])
        return js


class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestReportSetupAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir: TestReportSetupActionAssert | None = None
        """ The assertion to perform.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation: TestReportSetupActionOperation | None = None
        """ The operation to perform.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
        ])
        return js


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    The results of the assertion performed on the previous operations.
    """
    
    resource_type = "TestReportSetupActionAssert"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail: str | None = None
        """ A link to further details on the result.
        Type `str`. """
        
        self.message: str | None = None
        """ A message associated with the result.
        Type `str`. """
        
        self.result: str | None = None
        """ pass | skip | fail | warning | error.
        Type `str`. """
        
        super(TestReportSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.
    
    The operation performed.
    """
    
    resource_type = "TestReportSetupActionOperation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail: str | None = None
        """ A link to further details on the result.
        Type `str`. """
        
        self.message: str | None = None
        """ A message associated with the result.
        Type `str`. """
        
        self.result: str | None = None
        """ pass | skip | fail | warning | error.
        Type `str`. """
        
        super(TestReportSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js


class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.
    
    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """
    
    resource_type = "TestReportTeardown"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestReportTeardownAction] | None = None
        """ One or more teardown operations performed.
        List of `TestReportTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestReportTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
        ])
        return js


class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.
    
    The teardown action will only contain an operation.
    """
    
    resource_type = "TestReportTeardownAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation: TestReportSetupActionOperation | None = None
        """ The teardown operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
        ])
        return js


class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
    """
    
    resource_type = "TestReportTest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestReportTestAction] | None = None
        """ A test operation or assert that was performed.
        List of `TestReportTestAction` items (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Tracking/reporting short description of the test.
        Type `str`. """
        
        self.name: str | None = None
        """ Tracking/logging name of this test.
        Type `str`. """
        
        super(TestReportTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestReportTestAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir: TestReportSetupActionAssert | None = None
        """ The assertion performed.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation: TestReportSetupActionOperation | None = None
        """ The operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
        ])
        return js


from . import fhirdatetime
from . import fhirreference
from . import identifier
