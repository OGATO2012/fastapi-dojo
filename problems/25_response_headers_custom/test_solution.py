import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_25", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_data_returns_200():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {"data": []}


def test_get_data_has_total_count_header():
    response = client.get("/data")
    assert "x-total-count" in response.headers
    assert response.headers["x-total-count"] == "42"


def test_get_data_has_api_version_header():
    response = client.get("/data")
    assert "x-api-version" in response.headers
    assert response.headers["x-api-version"] == "1.0"
