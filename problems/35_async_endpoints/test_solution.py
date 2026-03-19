import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_35", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_async_data():
    response = client.get("/async-data")
    assert response.status_code == 200
    assert response.json() == {"data": "async result", "type": "async"}


def test_async_item():
    response = client.get("/async-items/5")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 5
    assert data["name"] == "Item 5"


def test_async_item_different_id():
    response = client.get("/async-items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["name"] == "Item 42"
