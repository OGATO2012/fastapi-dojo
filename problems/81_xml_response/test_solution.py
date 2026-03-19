import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_81_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_get_user_xml(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "application/xml" in response.headers["content-type"]
    assert "Alice" in response.text
    assert "alice@example.com" in response.text


def test_get_user_xml_contains_id(client):
    response = client.get("/users/1")
    assert "1" in response.text


def test_get_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404


def test_get_users_xml(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert "application/xml" in response.headers["content-type"]
    assert "Alice" in response.text
    assert "Bob" in response.text


def test_get_users_xml_emails(client):
    response = client.get("/users/")
    assert "alice@example.com" in response.text
    assert "bob@example.com" in response.text
