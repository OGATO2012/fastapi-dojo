import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_39", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app, raise_server_exceptions=False)


def test_valid_api_key():
    response = client.get("/protected", headers={"X-API-Key": "my-secret-api-key"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Access granted"


def test_invalid_api_key():
    response = client.get("/protected", headers={"X-API-Key": "wrong-key"})
    assert response.status_code == 403


def test_missing_api_key():
    response = client.get("/protected")
    assert response.status_code == 403
