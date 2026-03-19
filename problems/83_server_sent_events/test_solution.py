import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_83_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_events_content_type(client):
    response = client.get("/events")
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]


def test_events_content(client):
    response = client.get("/events")
    text = response.text
    for i in range(1, 6):
        assert f"data: event {i}" in text


def test_events_all_five(client):
    response = client.get("/events")
    for i in range(1, 6):
        assert f"data: event {i}\n\n" in response.text


def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
