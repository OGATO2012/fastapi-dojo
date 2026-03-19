import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_24", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_post_item_with_aliases():
    response = client.post("/items", json={"id": 1, "name": "test"})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert data["item_name"] == "test"


def test_post_item_different_values():
    response = client.post("/items", json={"id": 99, "name": "widget"})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 99
    assert data["item_name"] == "widget"


def test_post_item_missing_field():
    response = client.post("/items", json={"id": 1})
    assert response.status_code == 422
