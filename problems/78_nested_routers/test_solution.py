import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_78_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Alice"


def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"


def test_get_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404


def test_get_posts(client):
    response = client.get("/users/1/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Hello"


def test_get_posts_empty(client):
    response = client.get("/users/2/posts")
    assert response.status_code == 200
    assert response.json() == []


def test_create_post():
    module = _load_starter_fresh()
    fresh_client = TestClient(module.app, raise_server_exceptions=True)
    response = fresh_client.post("/users/2/posts", json={"title": "New Post"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Post"


def test_create_post_user_not_found(client):
    response = client.post("/users/999/posts", json={"title": "Ghost"})
    assert response.status_code == 404
