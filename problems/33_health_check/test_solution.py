import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_33", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_health_status_200():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_healthy():
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "healthy"


def test_health_has_timestamp():
    response = client.get("/health")
    data = response.json()
    assert "timestamp" in data


def test_health_has_uptime_seconds():
    response = client.get("/health")
    data = response.json()
    assert "uptime_seconds" in data
    assert isinstance(data["uptime_seconds"], (int, float))
