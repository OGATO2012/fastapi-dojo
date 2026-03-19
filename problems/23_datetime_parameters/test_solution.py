import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_23", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)

SAMPLE_EVENT = {
    "name": "Conference",
    "start_time": "2024-01-01T09:00:00",
    "end_time": "2024-01-01T11:00:00",
}


def test_post_event_returns_200():
    response = client.post("/events", json=SAMPLE_EVENT)
    assert response.status_code == 200


def test_post_event_returns_duration():
    response = client.post("/events", json=SAMPLE_EVENT)
    data = response.json()
    assert "duration_seconds" in data
    assert data["duration_seconds"] == 7200.0  # 2 hours


def test_post_event_returns_name():
    response = client.post("/events", json=SAMPLE_EVENT)
    data = response.json()
    assert data["name"] == "Conference"


def test_invalid_datetime_returns_422():
    response = client.post("/events", json={
        "name": "Bad Event",
        "start_time": "not-a-date",
        "end_time": "also-not-a-date",
    })
    assert response.status_code == 422
