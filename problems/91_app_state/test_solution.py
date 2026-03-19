import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_91_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_counter_initial(client):
    # After first request (which increments), counter should be 1
    response = client.get("/counter")
    assert response.status_code == 200
    data = response.json()
    assert "counter" in data
    assert data["counter"] >= 1


def test_counter_increments(client):
    r1 = client.get("/counter").json()["counter"]
    r2 = client.get("/counter").json()["counter"]
    assert r2 > r1


def test_reset(client):
    # Make several requests
    client.get("/counter")
    client.get("/counter")
    # Reset
    response = client.get("/reset")
    assert response.status_code == 200
    assert response.json()["counter"] == 0


def test_counter_after_reset(client):
    client.get("/counter")
    client.get("/reset")
    # Next request will increment from 0 to 1
    resp = client.get("/counter")
    assert resp.json()["counter"] == 1


def test_counter_response_structure(client):
    response = client.get("/counter")
    data = response.json()
    assert isinstance(data["counter"], int)
