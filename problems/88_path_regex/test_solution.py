import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_88_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


def test_valid_item_id(client):
    response = client.get("/items/abc-123")
    assert response.status_code == 200
    assert response.json() == {"item_id": "abc-123"}


def test_valid_item_id_xyz(client):
    response = client.get("/items/xyz-999")
    assert response.status_code == 200
    assert response.json()["item_id"] == "xyz-999"


def test_invalid_item_id_uppercase(client):
    response = client.get("/items/ABC-123")
    assert response.status_code == 422


def test_invalid_item_id_short(client):
    response = client.get("/items/ab-123")
    assert response.status_code == 422


def test_invalid_item_id_no_dash(client):
    response = client.get("/items/abc123")
    assert response.status_code == 422


def test_invalid_item_id_letters_after_dash(client):
    response = client.get("/items/abc-xyz")
    assert response.status_code == 422


def test_file_path_simple(client):
    response = client.get("/files/readme.txt")
    assert response.status_code == 200
    assert response.json() == {"file_path": "readme.txt"}


def test_file_path_nested(client):
    response = client.get("/files/some/nested/path/file.py")
    assert response.status_code == 200
    assert response.json()["file_path"] == "some/nested/path/file.py"
