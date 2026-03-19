import importlib.util
import os
import uuid

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_79_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_get_data_keys(client):
    response = client.get("/data")
    assert response.status_code == 200
    data = response.json()
    assert "datetime" in data
    assert "price" in data
    assert "id" in data


def test_get_data_types(client):
    response = client.get("/data")
    data = response.json()
    assert isinstance(data["price"], (int, float))
    assert isinstance(data["datetime"], str)
    assert isinstance(data["id"], str)
    uuid.UUID(data["id"])


def test_post_product(client):
    response = client.post("/products", json={"name": "Widget", "price": "9.99"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Widget"
    assert isinstance(data["price"], (int, float))
    assert abs(data["price"] - 9.99) < 0.01


def test_post_product_price_numeric(client):
    response = client.post("/products", json={"name": "Gadget", "price": "24.99"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["price"], (int, float))
