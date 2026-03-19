import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_26", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_list_users_status():
    response = client.get("/users/")
    assert response.status_code == 200


def test_list_users_returns_list_with_id_and_name():
    response = client.get("/users/")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "name" in data[0]


def test_list_items_status():
    response = client.get("/items/")
    assert response.status_code == 200


def test_list_items_returns_list_with_id_and_name():
    response = client.get("/items/")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "name" in data[0]
