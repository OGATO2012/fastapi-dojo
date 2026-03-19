import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_11", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_root_returns_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_response_has_process_time_header():
    response = client.get("/")
    assert "x-process-time" in response.headers


def test_process_time_is_numeric():
    response = client.get("/")
    value = response.headers.get("x-process-time")
    assert value is not None
    float(value)  # Should not raise
