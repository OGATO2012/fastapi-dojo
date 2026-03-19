import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_87_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


VALID_HEADERS = {"X-Token": "fake-super-secret-token"}


def test_items_no_token(client):
    response = client.get("/items")
    assert response.status_code == 422  # missing required header


def test_items_wrong_token(client):
    response = client.get("/items", headers={"X-Token": "bad-token"})
    assert response.status_code == 400


def test_items_valid_token(client):
    response = client.get("/items", headers=VALID_HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "language" in data


def test_items_language_default(client):
    response = client.get("/items", headers=VALID_HEADERS)
    assert response.json()["language"] == "en"


def test_items_language_custom(client):
    headers = {**VALID_HEADERS, "Accept-Language": "ja"}
    response = client.get("/items", headers=headers)
    assert response.json()["language"] == "ja"


def test_users_valid_token(client):
    response = client.get("/users", headers=VALID_HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert "language" in data


def test_users_wrong_token(client):
    response = client.get("/users", headers={"X-Token": "wrong"})
    assert response.status_code == 400
