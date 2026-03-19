import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_74_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_create_item(client):
    response = client.post("/items/", json={"name": "Widget"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Widget"
    assert data["is_deleted"] is False
    assert "id" in data


def test_soft_delete(client):
    create_resp = client.post("/items/", json={"name": "ToDelete"})
    item_id = create_resp.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Item soft deleted"


def test_deleted_item_not_in_active(client):
    create_resp = client.post("/items/", json={"name": "GoAway"})
    item_id = create_resp.json()["id"]
    client.delete(f"/items/{item_id}")
    response = client.get("/items/")
    ids = [i["id"] for i in response.json()]
    assert item_id not in ids


def test_deleted_item_in_deleted(client):
    create_resp = client.post("/items/", json={"name": "Archived"})
    item_id = create_resp.json()["id"]
    client.delete(f"/items/{item_id}")
    response = client.get("/items/deleted")
    ids = [i["id"] for i in response.json()]
    assert item_id in ids


def test_delete_not_found(client):
    response = client.delete("/items/999")
    assert response.status_code == 404
