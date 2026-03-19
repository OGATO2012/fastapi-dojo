import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    """Load starter.py as a fresh module (new global state each call)."""
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_09_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    """Each test gets a fresh app with an empty database."""
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_list_items_empty(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item(client):
    response = client.post("/items", json={"name": "apple", "description": "a fruit"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "apple"
    assert data["description"] == "a fruit"
    assert "id" in data


def test_create_and_list_items(client):
    client.post("/items", json={"name": "apple"})
    client.post("/items", json={"name": "banana"})
    response = client.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2
    names = [i["name"] for i in items]
    assert "apple" in names
    assert "banana" in names


def test_get_item(client):
    create_resp = client.post("/items", json={"name": "cherry"})
    item_id = create_resp.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "cherry"


def test_get_item_not_found(client):
    response = client.get("/items/9999")
    assert response.status_code == 404


def test_update_item(client):
    create_resp = client.post("/items", json={"name": "old name"})
    item_id = create_resp.json()["id"]
    response = client.put(f"/items/{item_id}", json={"name": "new name", "description": "updated"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "new name"
    assert data["description"] == "updated"
    assert data["id"] == item_id


def test_update_item_not_found(client):
    response = client.put("/items/9999", json={"name": "x"})
    assert response.status_code == 404


def test_delete_item(client):
    create_resp = client.post("/items", json={"name": "to delete"})
    item_id = create_resp.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    # Verify it's gone
    get_resp = client.get(f"/items/{item_id}")
    assert get_resp.status_code == 404


def test_delete_item_not_found(client):
    response = client.delete("/items/9999")
    assert response.status_code == 404
