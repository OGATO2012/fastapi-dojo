import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_07", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_existing_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "apple"}


def test_get_another_existing_item():
    response = client.get("/items/3")
    assert response.status_code == 200
    assert response.json() == {"id": 3, "name": "cherry"}


def test_get_nonexistent_item():
    response = client.get("/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_get_item_invalid_id():
    response = client.get("/items/abc")
    assert response.status_code == 422
