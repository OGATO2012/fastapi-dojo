import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_21", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)

SAMPLE_USER = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "zip_code": "12345",
    },
}


def test_post_user_returns_user():
    response = client.post("/users", json=SAMPLE_USER)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Alice"
    assert data["age"] == 30


def test_post_user_returns_nested_address():
    response = client.post("/users", json=SAMPLE_USER)
    assert response.status_code == 200
    data = response.json()
    assert "address" in data
    assert data["address"]["city"] == "Springfield"
    assert data["address"]["street"] == "123 Main St"


def test_post_user_invalid_missing_address():
    response = client.post("/users", json={"name": "Bob", "age": 25})
    assert response.status_code == 422
