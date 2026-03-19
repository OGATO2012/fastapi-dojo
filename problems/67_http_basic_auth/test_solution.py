import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_67_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_valid_credentials(client):
    response = client.get("/protected", auth=("user", "secret"))
    assert response.status_code == 200
    assert response.json() == {"username": "user"}


def test_invalid_password(client):
    response = client.get("/protected", auth=("user", "wrong"))
    assert response.status_code == 401


def test_invalid_username(client):
    response = client.get("/protected", auth=("wrong", "secret"))
    assert response.status_code == 401


def test_no_credentials():
    module = _load_starter_fresh()
    no_auth_client = TestClient(module.app, raise_server_exceptions=False)
    response = no_auth_client.get("/protected")
    assert response.status_code == 401
