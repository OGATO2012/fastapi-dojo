import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_69_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_v1_users(client):
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Alice"


def test_v2_users(client):
    response = client.get("/api/v2/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Alice"
    assert data[0]["email"] == "alice@example.com"


def test_v1_no_email(client):
    response = client.get("/api/v1/users")
    data = response.json()
    assert "email" not in data[0]


def test_v2_has_email(client):
    response = client.get("/api/v2/users")
    data = response.json()
    assert "email" in data[0]
