import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_89_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_user_all_fields(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert "password" in data


def test_user_field_selection(client):
    response = client.get("/users/1?fields=name,email")
    assert response.status_code == 200
    data = response.json()
    assert set(data.keys()) == {"name", "email"}
    assert data["name"] == "Alice"
    assert data["email"] == "alice@example.com"


def test_user_single_field(client):
    response = client.get("/users/1?fields=name")
    assert response.status_code == 200
    data = response.json()
    assert list(data.keys()) == ["name"]


def test_user_public_no_password(client):
    response = client.get("/users/1/public")
    assert response.status_code == 200
    data = response.json()
    assert "password" not in data
    assert "name" in data
    assert "email" in data


def test_user_public_fields(client):
    response = client.get("/users/2/public")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bob"
    assert data["id"] == 2


def test_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404
