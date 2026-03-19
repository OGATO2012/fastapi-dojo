import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_99_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


def test_login_valid_key(client):
    response = client.post("/auth/login?api_key=secret")
    assert response.status_code == 200
    assert "auth_token" in response.cookies


def test_login_invalid_key(client):
    response = client.post("/auth/login?api_key=wrong")
    assert response.status_code == 401


def test_login_no_key(client):
    response = client.post("/auth/login")
    assert response.status_code == 422


def test_protected_no_cookie(client):
    response = client.get("/auth/protected")
    assert response.status_code == 401


def test_protected_with_valid_cookie(client):
    response = client.get(
        "/auth/protected",
        cookies={"auth_token": "authenticated_user_token"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["user"] == "authenticated"
    assert data["message"] == "access granted"


def test_protected_with_wrong_cookie(client):
    response = client.get(
        "/auth/protected",
        cookies={"auth_token": "wrong_token"},
    )
    assert response.status_code == 401


def test_logout(client):
    response = client.post("/auth/logout")
    assert response.status_code == 200
    assert response.json() == {"message": "logged out"}
