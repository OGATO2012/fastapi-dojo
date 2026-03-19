import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_22", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)

VALID_PRODUCT = {"name": "Widget", "price": 9.99, "quantity": 50}


def test_valid_product_returns_200():
    response = client.post("/products", json=VALID_PRODUCT)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Widget"


def test_short_name_returns_422():
    response = client.post("/products", json={"name": "AB", "price": 9.99, "quantity": 10})
    assert response.status_code == 422


def test_negative_price_returns_422():
    response = client.post("/products", json={"name": "Widget", "price": -1.0, "quantity": 10})
    assert response.status_code == 422


def test_zero_price_returns_422():
    response = client.post("/products", json={"name": "Widget", "price": 0.0, "quantity": 10})
    assert response.status_code == 422


def test_quantity_over_100_returns_422():
    response = client.post("/products", json={"name": "Widget", "price": 9.99, "quantity": 101})
    assert response.status_code == 422


def test_quantity_zero_is_valid():
    response = client.post("/products", json={"name": "Widget", "price": 9.99, "quantity": 0})
    assert response.status_code == 200
