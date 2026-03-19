import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_72_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_strict_strips_whitespace(client):
    response = client.post("/users/strict", json={"name": "  Alice  ", "email": "  alice@test.com  "})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@test.com"


def test_strict_empty_string_fails(client):
    response = client.post("/users/strict", json={"name": "", "email": "test@test.com"})
    assert response.status_code == 422


def test_frozen_user(client):
    response = client.post("/users/frozen", json={"name": "Alice", "email": "alice@test.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@test.com"


def test_frozen_immutable():
    module = _load_starter_fresh()
    user = module.UserFrozen(name="Alice", email="alice@test.com")
    with pytest.raises(Exception):
        user.name = "Bob"
