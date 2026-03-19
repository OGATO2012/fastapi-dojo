import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_59", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_valid_user():
    response = client.post("/users/", json={"username": "Alice123", "email": "Alice@Example.com", "age": 25})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice123"
    assert data["email"] == "alice@example.com"

def test_invalid_username_special_chars():
    response = client.post("/users/", json={"username": "alice!", "email": "alice@example.com", "age": 25})
    assert response.status_code == 422

def test_invalid_email_no_at():
    response = client.post("/users/", json={"username": "alice", "email": "aliceexample.com", "age": 25})
    assert response.status_code == 422

def test_negative_age():
    response = client.post("/users/", json={"username": "alice", "email": "alice@example.com", "age": -1})
    assert response.status_code == 422

def test_age_over_150():
    response = client.post("/users/", json={"username": "alice", "email": "alice@example.com", "age": 200})
    assert response.status_code == 422
