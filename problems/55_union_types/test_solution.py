import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_55", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_post_cat():
    cat_data = {"type": "cat", "name": "Whiskers", "indoor": True}
    response = client.post("/animals/", json=cat_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Whiskers"
    assert data["indoor"] is True


def test_post_dog():
    dog_data = {"type": "dog", "name": "Rex", "breed": "German Shepherd"}
    response = client.post("/animals/", json=dog_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Rex"
    assert data["breed"] == "German Shepherd"


def test_get_pets():
    response = client.get("/pets/")
    assert response.status_code == 200
    pets = response.json()
    assert len(pets) == 2
