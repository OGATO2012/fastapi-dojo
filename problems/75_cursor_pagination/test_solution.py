import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_75_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_first_page(client):
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 10
    assert data["next_cursor"] == 10


def test_second_page(client):
    response = client.get("/items?cursor=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 10
    ids = [item["id"] for item in data["items"]]
    assert ids == list(range(11, 21))
    assert data["next_cursor"] is None


def test_custom_limit(client):
    response = client.get("/items?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 5
    assert data["next_cursor"] == 5


def test_cursor_with_limit(client):
    response = client.get("/items?cursor=15&limit=5")
    assert response.status_code == 200
    data = response.json()
    ids = [item["id"] for item in data["items"]]
    assert ids == [16, 17, 18, 19, 20]
    assert data["next_cursor"] is None
