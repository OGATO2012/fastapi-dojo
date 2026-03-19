import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_08", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_list_users_defaults():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"resource": "users", "skip": 0, "limit": 10}


def test_list_users_with_params():
    response = client.get("/users?skip=5&limit=20")
    assert response.status_code == 200
    assert response.json() == {"resource": "users", "skip": 5, "limit": 20}


def test_list_items_defaults():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"resource": "items", "skip": 0, "limit": 10}


def test_list_items_with_params():
    response = client.get("/items?skip=10&limit=5")
    assert response.status_code == 200
    assert response.json() == {"resource": "items", "skip": 10, "limit": 5}
