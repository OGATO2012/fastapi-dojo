import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_27", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_default_pagination():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 10
    assert data["total"] == 100
    assert data["skip"] == 0
    assert data["limit"] == 10


def test_custom_limit():
    response = client.get("/items/?skip=0&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 5


def test_skip_and_limit():
    response = client.get("/items/?skip=10&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 5
    assert data["items"][0]["name"] == "Item 11"
