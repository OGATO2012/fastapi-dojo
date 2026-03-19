import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_97_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_items_no_tags(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"tags": []}


def test_items_single_tag(client):
    response = client.get("/items?tags=foo")
    assert response.status_code == 200
    assert response.json() == {"tags": ["foo"]}


def test_items_multiple_tags(client):
    response = client.get("/items?tags=foo&tags=bar&tags=baz")
    assert response.status_code == 200
    assert response.json() == {"tags": ["foo", "bar", "baz"]}


def test_ids_no_ids(client):
    response = client.get("/ids")
    assert response.status_code == 200
    assert response.json() == {"ids": []}


def test_ids_single(client):
    response = client.get("/ids?ids=42")
    assert response.status_code == 200
    assert response.json() == {"ids": [42]}


def test_ids_multiple(client):
    response = client.get("/ids?ids=1&ids=2&ids=3")
    assert response.status_code == 200
    assert response.json() == {"ids": [1, 2, 3]}


def test_ids_invalid_type(client):
    response = client.get("/ids?ids=abc")
    assert response.status_code == 422
