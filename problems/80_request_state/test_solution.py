import importlib.util
import os
import uuid

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_80_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_info_keys(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "request_id" in data
    assert "processing_time" in data


def test_request_id_is_uuid(client):
    response = client.get("/info")
    data = response.json()
    uuid.UUID(data["request_id"])


def test_processing_time_non_negative(client):
    response = client.get("/info")
    data = response.json()
    assert data["processing_time"] >= 0


def test_request_id_unique():
    module = _load_starter_fresh()
    c = TestClient(module.app, raise_server_exceptions=True)
    r1 = c.get("/info").json()["request_id"]
    r2 = c.get("/info").json()["request_id"]
    assert r1 != r2
