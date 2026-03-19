import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_66_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_partial_update_name(client):
    response = client.patch("/users/1", json={"name": "Bob"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bob"
    assert data["email"] == "alice@example.com"
    assert data["age"] == 30


def test_partial_update_email(client):
    response = client.patch("/users/1", json={"email": "new@test.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "new@test.com"
    assert data["name"] == "Alice"
    assert data["age"] == 30


def test_partial_update_multiple(client):
    response = client.patch("/users/1", json={"name": "Charlie", "age": 25})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Charlie"
    assert data["age"] == 25
    assert data["email"] == "alice@example.com"


def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"


def test_user_not_found(client):
    response = client.patch("/users/999", json={"name": "Ghost"})
    assert response.status_code == 404
