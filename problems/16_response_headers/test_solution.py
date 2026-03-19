import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_16", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_items_returns_empty_list():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": []}


def test_items_has_custom_header():
    response = client.get("/items")
    assert "x-custom-header" in response.headers


def test_custom_header_value():
    response = client.get("/items")
    assert response.headers["x-custom-header"] == "my-value"
