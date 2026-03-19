import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_29", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_no_sort_returns_original_order():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == "Cherry"


def test_sort_by_name_asc():
    response = client.get("/items/?sort_by=name&order=asc")
    assert response.status_code == 200
    data = response.json()
    names = [item["name"] for item in data]
    assert names == ["Apple", "Banana", "Cherry"]


def test_sort_by_price_desc():
    response = client.get("/items/?sort_by=price&order=desc")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["name"] == "Cherry"
    assert data[0]["price"] == 3.0
    assert data[1]["name"] == "Banana"
    assert data[2]["name"] == "Apple"
