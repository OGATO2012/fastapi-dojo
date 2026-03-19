import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_57", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_get_users_default_page():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert "page" in data
    assert "size" in data
    assert data["page"] == 1
    assert data["size"] == 3

def test_get_users_page2():
    response = client.get("/users/?page=2&size=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert data["size"] == 2
    assert len(data["items"]) == 2

def test_get_products_default():
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert len(data["items"]) <= 3

def test_get_products_page2():
    response = client.get("/products/?page=2&size=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
