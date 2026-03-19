import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_38", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_create_token():
    response = client.post("/create-token", json={"username": "alice"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_verify_valid_token():
    create_resp = client.post("/create-token", json={"username": "alice"})
    token = create_resp.json()["access_token"]
    verify_resp = client.post("/verify-token", json={"token": token})
    assert verify_resp.status_code == 200
    data = verify_resp.json()
    assert data["valid"] is True
    assert data["username"] == "alice"


def test_verify_invalid_token():
    response = client.post("/verify-token", json={"token": "invalid.token.here"})
    assert response.status_code == 401
