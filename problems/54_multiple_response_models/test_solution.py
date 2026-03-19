import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_54", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_existing_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Apple"
    assert data["price"] == 1.5


def test_get_missing_item():
    response = client.get("/items/999")
    assert response.status_code == 404


def test_openapi_has_multiple_responses():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    paths = response.json()["paths"]
    item_path = paths["/items/{item_id}"]["get"]["responses"]
    assert "200" in item_path
    assert "404" in item_path
