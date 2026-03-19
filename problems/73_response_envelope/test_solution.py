import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_73_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_get_user_envelope(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["id"] == 1
    assert data["data"]["name"] == "Alice"
    assert data["message"] == "User found"


def test_get_users_list(client):
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert isinstance(data["data"], list)
    assert len(data["data"]) == 2


def test_user_not_found_envelope(client):
    response = client.get("/users/99")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert data["message"] == "User not found"
