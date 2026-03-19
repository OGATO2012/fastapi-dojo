import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_37", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_hash_password_returns_hashed():
    response = client.post("/hash-password", json={"password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert "hashed_password" in data
    assert data["hashed_password"] != "secret"
    assert len(data["hashed_password"]) > 10


def test_verify_correct_password():
    hash_resp = client.post("/hash-password", json={"password": "mypassword"})
    hashed = hash_resp.json()["hashed_password"]
    verify_resp = client.post("/verify-password", json={"password": "mypassword", "hashed_password": hashed})
    assert verify_resp.status_code == 200
    assert verify_resp.json()["is_valid"] is True


def test_verify_wrong_password():
    hash_resp = client.post("/hash-password", json={"password": "mypassword"})
    hashed = hash_resp.json()["hashed_password"]
    verify_resp = client.post("/verify-password", json={"password": "wrongpassword", "hashed_password": hashed})
    assert verify_resp.status_code == 200
    assert verify_resp.json()["is_valid"] is False
