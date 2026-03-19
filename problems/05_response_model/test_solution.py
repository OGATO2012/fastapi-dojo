import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_05", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_create_user_hides_password():
    payload = {"username": "alice", "password": "secret123", "email": "alice@example.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert "password" not in data


def test_create_user_missing_username():
    payload = {"password": "secret123", "email": "alice@example.com"}
    response = client.post("/users", json=payload)
    assert response.status_code == 422
