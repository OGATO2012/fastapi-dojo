import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_03", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_list_items_defaults():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"skip": 0, "limit": 10, "keyword": None}


def test_list_items_with_params():
    response = client.get("/items?skip=5&limit=20&keyword=python")
    assert response.status_code == 200
    assert response.json() == {"skip": 5, "limit": 20, "keyword": "python"}


def test_list_items_partial_params():
    response = client.get("/items?limit=5")
    assert response.status_code == 200
    assert response.json() == {"skip": 0, "limit": 5, "keyword": None}


def test_list_items_invalid_skip():
    response = client.get("/items?skip=abc")
    assert response.status_code == 422
