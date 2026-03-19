import importlib.util
import os
import uuid
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_100_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_info_has_request_id(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "request_id" in data


def test_info_request_id_is_uuid(client):
    response = client.get("/info")
    request_id = response.json()["request_id"]
    uuid.UUID(request_id)  # Should not raise


def test_info_request_id_unique():
    module = _load_starter_fresh()
    c = TestClient(module.app)
    r1 = c.get("/info").json()["request_id"]
    r2 = c.get("/info").json()["request_id"]
    assert r1 != r2


def test_info_has_config(client):
    response = client.get("/info")
    data = response.json()
    assert "config" in data
    config = data["config"]
    assert config["app_name"] == "FastAPI Dojo"


def test_info_same_config(client):
    # get_config should return the same object - FastAPI deduplicates same dependencies
    response = client.get("/info")
    data = response.json()
    assert data["same_config"] is True


def test_config_consistent_across_requests(client):
    r1 = client.get("/info").json()["config"]
    r2 = client.get("/info").json()["config"]
    assert r1 == r2
