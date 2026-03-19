import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_58", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_valid_date_range():
    response = client.post("/date-range", json={"start_date": "2024-01-01", "end_date": "2024-12-31"})
    assert response.status_code == 200
    data = response.json()
    assert data["valid"] == True

def test_invalid_date_range():
    response = client.post("/date-range", json={"start_date": "2024-12-31", "end_date": "2024-01-01"})
    assert response.status_code == 422

def test_equal_dates_invalid():
    response = client.post("/date-range", json={"start_date": "2024-06-01", "end_date": "2024-06-01"})
    assert response.status_code == 422

def test_matching_passwords():
    response = client.post("/register", json={"username": "alice", "password": "secret123", "confirm_password": "secret123"})
    assert response.status_code == 200
    data = response.json()
    assert data["registered"] == True

def test_mismatched_passwords():
    response = client.post("/register", json={"username": "alice", "password": "secret123", "confirm_password": "wrong"})
    assert response.status_code == 422
