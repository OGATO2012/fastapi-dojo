import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_06", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_create_item_returns_201():
    response = client.post("/items", json={"name": "book"})
    assert response.status_code == 201
    assert response.json() == {"name": "book", "id": 1}


def test_delete_item_returns_204():
    response = client.delete("/items/1")
    assert response.status_code == 204
    assert response.content == b""
