import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_76_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_bulk_delete_existing(client):
    response = client.post("/items/bulk-delete", json={"ids": [1, 2, 3]})
    assert response.status_code == 200
    data = response.json()
    assert sorted(data["deleted"]) == [1, 2, 3]
    assert data["not_found"] == []


def test_bulk_delete_not_found(client):
    response = client.post("/items/bulk-delete", json={"ids": [10, 20]})
    assert response.status_code == 200
    data = response.json()
    assert data["deleted"] == []
    assert sorted(data["not_found"]) == [10, 20]


def test_bulk_delete_mixed():
    module = _load_starter_fresh()
    fresh_client = TestClient(module.app, raise_server_exceptions=True)
    response = fresh_client.post("/items/bulk-delete", json={"ids": [1, 99, 3]})
    assert response.status_code == 200
    data = response.json()
    assert sorted(data["deleted"]) == [1, 3]
    assert data["not_found"] == [99]


def test_bulk_delete_removes_item():
    module = _load_starter_fresh()
    fresh_client = TestClient(module.app, raise_server_exceptions=True)
    fresh_client.post("/items/bulk-delete", json={"ids": [1]})
    response = fresh_client.post("/items/bulk-delete", json={"ids": [1]})
    assert response.status_code == 200
    data = response.json()
    assert data["deleted"] == []
    assert data["not_found"] == [1]
