import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_98_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_fast_response(client):
    response = client.get("/fast")
    assert response.status_code == 200
    assert response.json() == {"message": "fast response"}


def test_fast_has_process_time_header(client):
    response = client.get("/fast")
    assert "x-process-time" in response.headers


def test_process_time_is_float(client):
    response = client.get("/fast")
    val = float(response.headers["x-process-time"])
    assert val >= 0


def test_slow_response(client):
    response = client.get("/slow?delay=0.05")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "slow response"
    assert data["delay"] == 0.05


def test_slow_has_process_time_header(client):
    response = client.get("/slow?delay=0.05")
    assert "x-process-time" in response.headers


def test_slow_process_time_greater_than_delay(client):
    response = client.get("/slow?delay=0.05")
    process_time = float(response.headers["x-process-time"])
    assert process_time >= 0.05


def test_slow_default_delay(client):
    response = client.get("/slow")
    assert response.status_code == 200
    assert response.json()["delay"] == 0.1
