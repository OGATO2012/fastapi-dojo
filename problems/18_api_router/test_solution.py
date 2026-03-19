import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_18", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_items_list():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) > 0


def test_get_item_by_id():
    response = client.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42


def test_get_item_returns_name():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
