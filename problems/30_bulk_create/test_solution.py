import importlib.util, os, pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_30", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_bulk_create_returns_count(client):
    response = client.post("/items/bulk", json=[
        {"name": "Apple", "price": 1.5},
        {"name": "Banana", "price": 2.0},
    ])
    assert response.status_code == 201
    data = response.json()
    assert data["count"] == 2
    assert len(data["created"]) == 2


def test_bulk_create_assigns_ids(client):
    response = client.post("/items/bulk", json=[
        {"name": "Cherry", "price": 3.0},
    ])
    assert response.status_code == 201
    data = response.json()
    assert "id" in data["created"][0]


def test_list_items_after_bulk_create(client):
    client.post("/items/bulk", json=[
        {"name": "Apple", "price": 1.5},
        {"name": "Banana", "price": 2.0},
    ])
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2
    names = [item["name"] for item in items]
    assert "Apple" in names
    assert "Banana" in names
