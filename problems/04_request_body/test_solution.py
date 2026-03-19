import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_04", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_create_item():
    response = client.post("/items", json={"name": "apple", "price": 1.5})
    assert response.status_code == 200
    assert response.json() == {"name": "apple", "price": 1.5, "in_stock": True}


def test_create_item_explicit_in_stock():
    response = client.post("/items", json={"name": "orange", "price": 2.0, "in_stock": False})
    assert response.status_code == 200
    assert response.json() == {"name": "orange", "price": 2.0, "in_stock": False}


def test_create_item_missing_required_field():
    response = client.post("/items", json={"price": 1.5})
    assert response.status_code == 422


def test_create_item_invalid_price():
    response = client.post("/items", json={"name": "apple", "price": "not-a-number"})
    assert response.status_code == 422
