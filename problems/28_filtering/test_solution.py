import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_28", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_no_filter_returns_all():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_filter_fruit():
    response = client.get("/items/?category=fruit")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(item["category"] == "fruit" for item in data)


def test_filter_vegetable():
    response = client.get("/items/?category=vegetable")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(item["category"] == "vegetable" for item in data)


def test_unknown_category_returns_empty():
    response = client.get("/items/?category=meat")
    assert response.status_code == 200
    assert response.json() == []
