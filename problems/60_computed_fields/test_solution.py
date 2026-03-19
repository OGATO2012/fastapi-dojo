import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_60", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_rectangle_area_perimeter():
    response = client.post("/rectangle/", json={"width": 3.0, "height": 4.0})
    assert response.status_code == 200
    data = response.json()
    assert data["area"] == 12.0
    assert data["perimeter"] == 14.0

def test_rectangle_square():
    response = client.post("/rectangle/", json={"width": 5.0, "height": 5.0})
    assert response.status_code == 200
    data = response.json()
    assert data["area"] == 25.0
    assert data["perimeter"] == 20.0

def test_cart_totals():
    items = [{"name": "apple", "price": 1.5}, {"name": "bread", "price": 2.5}, {"name": "milk", "price": 3.0}]
    response = client.post("/cart/", json={"items": items})
    assert response.status_code == 200
    data = response.json()
    assert data["item_count"] == 3
    assert data["total_price"] == 7.0

def test_empty_cart():
    response = client.post("/cart/", json={"items": []})
    assert response.status_code == 200
    data = response.json()
    assert data["item_count"] == 0
    assert data["total_price"] == 0.0
