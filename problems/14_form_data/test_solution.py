import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_14", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_submit_form_returns_json():
    response = client.post("/submit", data={"name": "Alice", "age": "30"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["age"] == 30


def test_submit_form_different_values():
    response = client.post("/submit", data={"name": "Bob", "age": "25"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bob"
    assert data["age"] == 25


def test_submit_form_missing_field():
    response = client.post("/submit", data={"name": "Alice"})
    assert response.status_code == 422
