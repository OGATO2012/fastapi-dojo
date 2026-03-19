import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_62", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_valid_item():
    response = client.post("/items/", json={"name": "Apple", "price": 1.5, "quantity": 10})
    assert response.status_code == 200

def test_invalid_item_custom_error_format():
    response = client.post("/items/", json={"name": "Apple", "price": "not-a-number", "quantity": "also-not-a-number"})
    assert response.status_code == 422
    data = response.json()
    assert "errors" in data
    assert "message" in data
    assert data["message"] == "Validation failed"

def test_invalid_item_errors_structure():
    response = client.post("/items/", json={"price": "bad", "quantity": -1})
    assert response.status_code == 422
    data = response.json()
    assert isinstance(data["errors"], list)
    if len(data["errors"]) > 0:
        error = data["errors"][0]
        assert "field" in error
        assert "message" in error
        assert "type" in error
