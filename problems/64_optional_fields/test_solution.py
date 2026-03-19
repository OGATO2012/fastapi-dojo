import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_64", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_minimal_profile():
    response = client.post("/profiles/", json={"username": "bob", "email": "bob@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "bob"
    assert data["bio"] is None
    assert data["is_active"] == True

def test_full_profile():
    response = client.post("/profiles/", json={"username": "charlie", "email": "charlie@example.com", "bio": "Hello", "age": 30, "is_active": False})
    assert response.status_code == 200
    data = response.json()
    assert data["bio"] == "Hello"
    assert data["age"] == 30
    assert data["is_active"] == False

def test_sample_profile():
    response = client.get("/profiles/sample")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["is_active"] == True
