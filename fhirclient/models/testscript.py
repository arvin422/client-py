# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TestScript).
# 2024, SMART Health IT.

from __future__ import annotations

from .fhirabstractbase import FHIRProperty, JSONValue


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.
    
    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """
    
    resource_type = "TestScript"
    
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
        """ Natural language description of the test script.
        Type `str`. """
        
        self.destination: list[TestScriptDestination] | None = None
        """ An abstract server representing a destination or receiver in a
        message exchange.
        List of `TestScriptDestination` items (represented as `dict` in JSON). """
        
        self.experimental: bool | None = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.fixture: list[TestScriptFixture] | None = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """
        
        self.identifier: identifier.Identifier | None = None
        """ Additional identifier for the test script.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.jurisdiction: list[codeableconcept.CodeableConcept] | None = None
        """ Intended jurisdiction for test script (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.metadata: TestScriptMetadata | None = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
        self.name: str | None = None
        """ Name for this test script (computer friendly).
        Type `str`. """
        
        self.origin: list[TestScriptOrigin] | None = None
        """ An abstract server representing a client or sender in a message
        exchange.
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """
        
        self.profile: list[fhirreference.FHIRReference] | None = None
        """ Reference of the validation profile.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.publisher: str | None = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.purpose: str | None = None
        """ Why this test script is defined.
        Type `str`. """
        
        self.setup: TestScriptSetup | None = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """
        
        self.status: str | None = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.teardown: TestScriptTeardown | None = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """
        
        self.test: list[TestScriptTest] | None = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """
        
        self.title: str | None = None
        """ Name for this test script (human friendly).
        Type `str`. """
        
        self.url: str | None = None
        """ Canonical identifier for this test script, represented as a URI
        (globally unique).
        Type `str`. """
        
        self.useContext: list[usagecontext.UsageContext] | None = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.variable: list[TestScriptVariable] | None = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """
        
        self.version: str | None = None
        """ Business version of the test script.
        Type `str`. """
        
        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("description", "description", str, False, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("name", "name", str, False, None, True),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.
    
    An abstract server used in operations within this test script in the
    destination element.
    """
    
    resource_type = "TestScriptDestination"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index: int | None = None
        """ The index of the abstract destination server starting at 1.
        Type `int`. """
        
        self.profile: coding.Coding | None = None
        """ FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-
        SDC-FormProcessor.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).
    
    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """
    
    resource_type = "TestScriptFixture"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.autocreate: bool | None = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """
        
        self.autodelete: bool | None = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """
        
        self.resource: fhirreference.FHIRReference | None = None
        """ Reference of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("autodelete", "autodelete", bool, False, None, True),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.
    
    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """
    
    resource_type = "TestScriptMetadata"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capability: list[TestScriptMetadataCapability] | None = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """
        
        self.link: list[TestScriptMetadataLink] | None = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """
        
        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
            ("link", "link", TestScriptMetadataLink, True, None, False),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.
    
    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """
    
    resource_type = "TestScriptMetadataCapability"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capabilities: str | None = None
        """ Required Capability Statement.
        Type `str`. """
        
        self.description: str | None = None
        """ The expected capabilities of the server.
        Type `str`. """
        
        self.destination: int | None = None
        """ Which server these requirements apply to.
        Type `int`. """
        
        self.link: list[str | None] | None = None
        """ Links to the FHIR specification.
        List of `str` items. """
        
        self.origin: list[int | None] | None = None
        """ Which origin server these requirements apply to.
        List of `int` items. """
        
        self.required: bool | None = None
        """ Are the capabilities required?.
        Type `bool`. """
        
        self.validated: bool | None = None
        """ Are the capabilities validated?.
        Type `bool`. """
        
        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("capabilities", "capabilities", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", str, True, None, False),
            ("origin", "origin", int, True, None, False),
            ("required", "required", bool, False, None, True),
            ("validated", "validated", bool, False, None, True),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.
    
    A link to the FHIR specification that this test is covering.
    """
    
    resource_type = "TestScriptMetadataLink"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description: str | None = None
        """ Short description.
        Type `str`. """
        
        self.url: str | None = None
        """ URL to the specification.
        Type `str`. """
        
        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("url", "url", str, False, None, True),
        ])
        return js


class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.
    
    An abstract server used in operations within this test script in the origin
    element.
    """
    
    resource_type = "TestScriptOrigin"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index: int | None = None
        """ The index of the abstract origin server starting at 1.
        Type `int`. """
        
        self.profile: coding.Coding | None = None
        """ FHIR-Client | FHIR-SDC-FormFiller.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """
    
    resource_type = "TestScriptSetup"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestScriptSetupAction] | None = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """
        
        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestScriptSetupAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir: TestScriptSetupActionAssert | None = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation: TestScriptSetupActionOperation | None = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.
    
    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """
    
    resource_type = "TestScriptSetupActionAssert"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compareToSourceExpression: str | None = None
        """ The FHIRPath expression to evaluate against the source fixture.
        Type `str`. """
        
        self.compareToSourceId: str | None = None
        """ Id of the source fixture to be evaluated.
        Type `str`. """
        
        self.compareToSourcePath: str | None = None
        """ XPath or JSONPath expression to evaluate against the source fixture.
        Type `str`. """
        
        self.contentType: str | None = None
        """ Mime type to compare against the 'Content-Type' header.
        Type `str`. """
        
        self.description: str | None = None
        """ Tracking/reporting assertion description.
        Type `str`. """
        
        self.direction: str | None = None
        """ response | request.
        Type `str`. """
        
        self.expression: str | None = None
        """ The FHIRPath expression to be evaluated.
        Type `str`. """
        
        self.headerField: str | None = None
        """ HTTP header field name.
        Type `str`. """
        
        self.label: str | None = None
        """ Tracking/logging assertion label.
        Type `str`. """
        
        self.minimumId: str | None = None
        """ Fixture Id of minimum content resource.
        Type `str`. """
        
        self.navigationLinks: bool | None = None
        """ Perform validation on navigation links?.
        Type `bool`. """
        
        self.operator: str | None = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains | eval.
        Type `str`. """
        
        self.path: str | None = None
        """ XPath or JSONPath expression.
        Type `str`. """
        
        self.requestMethod: str | None = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """
        
        self.requestURL: str | None = None
        """ Request URL comparison value.
        Type `str`. """
        
        self.resource: str | None = None
        """ Resource type.
        Type `str`. """
        
        self.response: str | None = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """
        
        self.responseCode: str | None = None
        """ HTTP response code to test.
        Type `str`. """
        
        self.sourceId: str | None = None
        """ Fixture Id of source expression or headerField.
        Type `str`. """
        
        self.validateProfileId: str | None = None
        """ Profile Id of validation profile reference.
        Type `str`. """
        
        self.value: str | None = None
        """ The value to compare to.
        Type `str`. """
        
        self.warningOnly: bool | None = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """
        
        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("compareToSourceExpression", "compareToSourceExpression", str, False, None, False),
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("direction", "direction", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("requestMethod", "requestMethod", str, False, None, False),
            ("requestURL", "requestURL", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("response", "response", str, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.
    
    The operation to perform.
    """
    
    resource_type = "TestScriptSetupActionOperation"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accept: str | None = None
        """ Mime type to accept in the payload of the response, with charset
        etc..
        Type `str`. """
        
        self.contentType: str | None = None
        """ Mime type of the request payload contents, with charset etc..
        Type `str`. """
        
        self.description: str | None = None
        """ Tracking/reporting operation description.
        Type `str`. """
        
        self.destination: int | None = None
        """ Server responding to the request.
        Type `int`. """
        
        self.encodeRequestUrl: bool | None = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """
        
        self.label: str | None = None
        """ Tracking/logging operation label.
        Type `str`. """
        
        self.method: str | None = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """
        
        self.origin: int | None = None
        """ Server initiating the request.
        Type `int`. """
        
        self.params: str | None = None
        """ Explicitly defined path parameters.
        Type `str`. """
        
        self.requestHeader: list[TestScriptSetupActionOperationRequestHeader] | None = None
        """ Each operation can have one or more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """
        
        self.requestId: str | None = None
        """ Fixture Id of mapped request.
        Type `str`. """
        
        self.resource: str | None = None
        """ Resource type.
        Type `str`. """
        
        self.responseId: str | None = None
        """ Fixture Id of mapped response.
        Type `str`. """
        
        self.sourceId: str | None = None
        """ Fixture Id of body for PUT and POST requests.
        Type `str`. """
        
        self.targetId: str | None = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """
        
        self.type: coding.Coding | None = None
        """ The operation code type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.url: str | None = None
        """ Request URL.
        Type `str`. """
        
        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("accept", "accept", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("label", "label", str, False, None, False),
            ("method", "method", str, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("params", "params", str, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.
    
    Header elements would be used to set HTTP headers.
    """
    
    resource_type = "TestScriptSetupActionOperationRequestHeader"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.field: str | None = None
        """ HTTP header field name.
        Type `str`. """
        
        self.value: str | None = None
        """ HTTP headerfield value.
        Type `str`. """
        
        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.
    
    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """
    
    resource_type = "TestScriptTeardown"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestScriptTeardownAction] | None = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.
    
    The teardown action will only contain an operation.
    """
    
    resource_type = "TestScriptTeardownAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation: TestScriptSetupActionOperation | None = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
    """
    
    resource_type = "TestScriptTest"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action: list[TestScriptTestAction] | None = None
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """
        
        self.description: str | None = None
        """ Tracking/reporting short description of the test.
        Type `str`. """
        
        self.name: str | None = None
        """ Tracking/logging name of this test.
        Type `str`. """
        
        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.
    
    Action would contain either an operation or an assertion.
    """
    
    resource_type = "TestScriptTestAction"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir: TestScriptSetupActionAssert | None = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation: TestScriptSetupActionOperation | None = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.
    
    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """
    
    resource_type = "TestScriptVariable"
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.defaultValue: str | None = None
        """ Default, hard-coded, or user-defined value for this variable.
        Type `str`. """
        
        self.description: str | None = None
        """ Natural language description of the variable.
        Type `str`. """
        
        self.expression: str | None = None
        """ The FHIRPath expression against the fixture body.
        Type `str`. """
        
        self.headerField: str | None = None
        """ HTTP header field name for source.
        Type `str`. """
        
        self.hint: str | None = None
        """ Hint help text for default value to enter.
        Type `str`. """
        
        self.name: str | None = None
        """ Descriptive name for this variable.
        Type `str`. """
        
        self.path: str | None = None
        """ XPath or JSONPath against the fixture body.
        Type `str`. """
        
        self.sourceId: str | None = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """
        
        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self) -> list[FHIRProperty]:
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("defaultValue", "defaultValue", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("hint", "hint", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("path", "path", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactdetail
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import usagecontext
