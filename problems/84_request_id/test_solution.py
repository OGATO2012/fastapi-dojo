import importlib.util
import os
import uuid

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_84_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_hello(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


def test_hello_has_request_id_header(client):
    response = client.get("/hello")
    assert "x-request-id" in response.headers


def test_request_id_is_uuid(client):
    response = client.get("/hello")
    header_value = response.headers["x-request-id"]
    uuid.UUID(header_value)


def test_request_id_unique():
    module = _load_starter_fresh()
    c = TestClient(module.app, raise_server_exceptions=True)
    r1 = c.get("/hello").headers["x-request-id"]
    r2 = c.get("/hello").headers["x-request-id"]
    assert r1 != r2


def test_request_id_endpoint(client):
    response = client.get("/request-id")
    assert response.status_code == 200
    data = response.json()
    assert "request_id" in data
    uuid.UUID(data["request_id"])


def test_request_id_matches_header(client):
    response = client.get("/request-id")
    header_id = response.headers["x-request-id"]
    body_id = response.json()["request_id"]
    assert header_id == body_id
