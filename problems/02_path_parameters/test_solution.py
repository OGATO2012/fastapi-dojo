import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_02", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_user():
    response = client.get("/users/42")
    assert response.status_code == 200
    assert response.json() == {"user_id": 42}


def test_get_user_type_validation():
    response = client.get("/users/abc")
    assert response.status_code == 422


def test_get_item():
    response = client.get("/items/book")
    assert response.status_code == 200
    assert response.json() == {"item_name": "book"}


def test_get_item_with_spaces():
    response = client.get("/items/hello%20world")
    assert response.status_code == 200
    assert response.json() == {"item_name": "hello world"}
