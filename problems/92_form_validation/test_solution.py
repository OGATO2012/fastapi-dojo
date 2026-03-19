import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_92_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


VALID_DATA = {"username": "alice", "email": "alice@example.com", "age": "25"}


def test_register_valid(client):
    response = client.post("/register", data=VALID_DATA)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["email"] == "alice@example.com"
    assert data["age"] == 25


def test_register_short_username(client):
    response = client.post("/register", data={**VALID_DATA, "username": "ab"})
    assert response.status_code == 422


def test_register_invalid_email(client):
    response = client.post("/register", data={**VALID_DATA, "email": "notanemail"})
    assert response.status_code == 422


def test_register_underage(client):
    response = client.post("/register", data={**VALID_DATA, "age": "17"})
    assert response.status_code == 422


def test_register_missing_field(client):
    response = client.post("/register", data={"username": "alice", "email": "a@b.com"})
    assert response.status_code == 422


def test_register_exact_minimum_age(client):
    response = client.post("/register", data={**VALID_DATA, "age": "18"})
    assert response.status_code == 200
    assert response.json()["age"] == 18
