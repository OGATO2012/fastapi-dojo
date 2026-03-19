import importlib.util, os, pytest
from fastapi.testclient import TestClient

def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_63", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)

def test_valid_product(client):
    response = client.post("/products/", json={"name": "Widget", "price": 9.99, "stock": 50})
    assert response.status_code == 200
    assert response.json()["name"] == "Widget"

def test_invalid_product_custom_error(client):
    response = client.post("/products/", json={"name": "", "price": -1, "stock": -5})
    assert response.status_code == 422
    data = response.json()
    assert data["detail"] == "Validation Error"
    assert "errors" in data

def test_error_log_populated(client):
    client.post("/products/", json={"name": "", "price": -1.0, "stock": 0})
    log_response = client.get("/error-log")
    assert log_response.status_code == 200
    log = log_response.json()
    assert len(log) >= 1
    assert log[0]["path"] == "/products/"
    assert log[0]["error_count"] >= 1
