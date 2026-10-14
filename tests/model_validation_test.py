"""Exercise complete resources across parsing, edits and serialization."""

import pytest

from fhirclient.models.fhirabstractbase import FHIRValidationError
from fhirclient.models.observation import Observation
from fhirclient.models.patient import Patient


def test_observation_choices_are_exclusive_on_read_and_write():
    payload = {
        "resourceType": "Observation",
        "status": "final",
        "code": {"text": "Example"},
        "valueBoolean": False,
    }
    observation = Observation(payload)
    assert observation.as_json() == payload
    with pytest.raises(FHIRValidationError, match="Conflicting properties"):
        Observation(payload | {"valueString": "yes"})
    observation.valueString = "yes"
    with pytest.raises(FHIRValidationError, match="Conflicting properties"):
        observation.as_json()


def test_patient_preserves_primitive_extensions_and_partial_dates():
    payload = {
        "resourceType": "Patient",
        "active": False,
        "birthDate": "1980-02",
        "_birthDate": {
            "extension": [{"url": "urn:test:date", "valueString": "month"}]
        },
        "name": [{
            "family": "Example",
            "given": ["First", None],
            "_given": [None, {
                "extension": [{
                    "url": "urn:test:missing", "valueCode": "unknown"
                }]
            }],
        }],
    }
    patient = Patient(payload)
    assert patient.as_json() == payload
    patient.active = True
    assert patient.as_json() == payload | {"active": True}


def test_every_list_element_and_required_choice_is_validated():
    with pytest.raises(FHIRValidationError):
        Patient({"name": [{"given": ["Valid", 12]}]})
    patient = Patient({"name": [{"given": ["Valid"]}]})
    patient.name[0].given.append(12)
    with pytest.raises(FHIRValidationError):
        patient.as_json()
    with pytest.raises(FHIRValidationError):
        Observation({"resourceType": "Observation", "code": {"text": "x"}})
    value = Observation({
        "resourceType": "Observation",
        "_status": {"extension": [{
            "url": "urn:test:missing", "valueCode": "unknown"
        }]},
        "code": {"text": "x"},
    })
    assert "_status" in value.as_json()


def test_patient_preserves_names_with_shorter_primitive_metadata():
    payload = {
        "resourceType": "Patient",
        "id": "epic-original.patient-identifier",
        "name": [
            {"use": "official", "given": ["First", "Middle"]},
            {
                "use": "usual",
                "given": ["Preferred", "Middle"],
                "_given": [{
                    "extension": [{
                        "url": "urn:test:given-name",
                        "valueCode": "preferred",
                    }],
                }],
            },
        ],
    }
    patient = Patient(payload)
    assert patient.id == payload["id"]
    assert patient.as_json() == payload
    patient.name[1].given.append("Additional")
    assert patient.as_json()["name"][1] == {
        **payload["name"][1],
        "given": ["Preferred", "Middle", "Additional"],
    }
    with pytest.raises(FHIRValidationError):
        Patient({"name": [{"given": ["Valid", None]}]})
