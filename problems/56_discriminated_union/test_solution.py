import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_56", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_create_cat():
    response = client.post("/pets/", json={"pet_type": "cat", "name": "Kitty", "meows": True})
    assert response.status_code == 200
    data = response.json()
    assert data["pet_type"] == "cat"
    assert data["name"] == "Kitty"
    assert data["meows"] == True

def test_create_dog():
    response = client.post("/pets/", json={"pet_type": "dog", "name": "Rex", "barks": True})
    assert response.status_code == 200
    data = response.json()
    assert data["pet_type"] == "dog"
    assert data["name"] == "Rex"
    assert data["barks"] == True

def test_invalid_pet_type():
    response = client.post("/pets/", json={"pet_type": "fish", "name": "Nemo"})
    assert response.status_code == 422
