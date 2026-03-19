import importlib.util, os
from fastapi.testclient import TestClient

VALID_TOKEN = "fake-super-secret-token"


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_49", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_items_no_token_returns_422():
    response = client.get("/items/")
    assert response.status_code == 422


def test_items_wrong_token_returns_400():
    response = client.get("/items/", headers={"X-Token": "wrong"})
    assert response.status_code == 400


def test_items_valid_token_returns_200():
    response = client.get("/items/", headers={"X-Token": VALID_TOKEN})
    assert response.status_code == 200
    assert response.json() == [{"item": "Foo"}, {"item": "Bar"}]


def test_users_no_token_returns_422():
    response = client.get("/users/")
    assert response.status_code == 422


def test_users_valid_token_returns_200():
    response = client.get("/users/", headers={"X-Token": VALID_TOKEN})
    assert response.status_code == 200
    assert response.json() == [{"username": "Rick"}, {"username": "Morty"}]
