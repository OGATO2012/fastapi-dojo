import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_86_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


def test_secure_no_key(client):
    response = client.get("/secure")
    assert response.status_code == 401


def test_secure_wrong_key(client):
    response = client.get("/secure", headers={"X-API-Key": "wrong-key"})
    assert response.status_code == 401


def test_secure_correct_key(client):
    response = client.get("/secure", headers={"X-API-Key": "my-secret-key"})
    assert response.status_code == 200


def test_secure_response_body(client):
    response = client.get("/secure", headers={"X-API-Key": "my-secret-key"})
    data = response.json()
    assert "message" in data
    assert data["message"] == "Access granted"


def test_openapi_schema_has_security(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    # Security scheme should be defined
    assert "components" in schema
    assert "securitySchemes" in schema["components"]
