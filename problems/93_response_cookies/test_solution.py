import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_93_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


def test_login_sets_cookie(client):
    response = client.post("/login")
    assert response.status_code == 200
    assert "session" in response.cookies


def test_login_response_body(client):
    response = client.post("/login")
    assert response.json() == {"message": "logged in"}


def test_profile_without_cookie(client):
    response = client.get("/profile")
    assert response.status_code == 401


def test_profile_with_valid_cookie(client):
    # Login first to get cookie
    login_response = client.post("/login")
    assert "session" in login_response.cookies
    # Use cookie in profile request
    response = client.get("/profile", cookies={"session": "session_abc123"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"


def test_profile_with_wrong_cookie(client):
    response = client.get("/profile", cookies={"session": "wrong_token"})
    assert response.status_code == 401


def test_logout(client):
    response = client.post("/logout")
    assert response.status_code == 200
    assert response.json() == {"message": "logged out"}
