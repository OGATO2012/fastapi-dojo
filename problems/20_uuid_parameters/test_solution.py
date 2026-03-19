import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_20", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)

VALID_UUID = "a3f1e5c2-4b8d-4e7f-9c1a-2d3b5e6f7a8b"


def test_valid_uuid_returns_item():
    response = client.get(f"/items/{VALID_UUID}")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == VALID_UUID


def test_invalid_uuid_returns_422():
    response = client.get("/items/not-a-uuid")
    assert response.status_code == 422


def test_uuid_string_format():
    response = client.get(f"/items/{VALID_UUID}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["item_id"], str)
    assert len(data["item_id"]) == 36  # UUID string length
