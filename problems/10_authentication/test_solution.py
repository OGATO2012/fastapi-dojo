import importlib.util
import os

from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_10", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_login_success():
    response = client.post("/token", data={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["access_token"] == "alice"
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    response = client.post("/token", data={"username": "alice", "password": "wrong"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_login_unknown_user():
    response = client.post("/token", data={"username": "nobody", "password": "x"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_get_current_user():
    response = client.get("/users/me", headers={"Authorization": "Bearer alice"})
    assert response.status_code == 200
    assert response.json() == {"username": "alice"}


def test_get_current_user_invalid_token():
    response = client.get("/users/me", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}


def test_get_current_user_no_token():
    response = client.get("/users/me")
    assert response.status_code == 401
