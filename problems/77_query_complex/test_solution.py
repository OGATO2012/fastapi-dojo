import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_77_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_no_filters(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_min_price(client):
    response = client.get("/products?min_price=10.0")
    assert response.status_code == 200
    data = response.json()
    assert all(p["price"] >= 10.0 for p in data)
    assert len(data) == 3


def test_max_price(client):
    response = client.get("/products?max_price=10.0")
    assert response.status_code == 200
    data = response.json()
    assert all(p["price"] <= 10.0 for p in data)
    assert len(data) == 2


def test_in_stock_true(client):
    response = client.get("/products?in_stock=true")
    assert response.status_code == 200
    data = response.json()
    assert all(p["in_stock"] for p in data)
    assert len(data) == 3


def test_in_stock_false(client):
    response = client.get("/products?in_stock=false")
    assert response.status_code == 200
    data = response.json()
    assert all(not p["in_stock"] for p in data)
    assert len(data) == 2


def test_single_category(client):
    response = client.get("/products?categories=tools")
    assert response.status_code == 200
    data = response.json()
    assert all(p["category"] == "tools" for p in data)
    assert len(data) == 2


def test_multiple_categories(client):
    response = client.get("/products?categories=tools&categories=electronics")
    assert response.status_code == 200
    data = response.json()
    assert all(p["category"] in ("tools", "electronics") for p in data)
    assert len(data) == 4


def test_combined_filters(client):
    response = client.get("/products?in_stock=true&categories=tools")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(p["in_stock"] and p["category"] == "tools" for p in data)
