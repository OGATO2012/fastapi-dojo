import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_90_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_admin_dashboard_accessible(client):
    response = client.get("/admin/dashboard")
    assert response.status_code == 200
    data = response.json()
    assert "dashboard" in data
    assert "user" in data


def test_admin_dashboard_username(client):
    response = client.get("/admin/dashboard")
    data = response.json()
    assert data["user"] == "alice"


def test_user_profile(client):
    response = client.get("/user/profile")
    assert response.status_code == 200
    data = response.json()
    assert "profile" in data


def test_user_profile_has_username(client):
    response = client.get("/user/profile")
    data = response.json()
    assert data["profile"]["username"] == "alice"


def test_dependency_chain_data():
    # Test that admin can access dashboard (alice is admin)
    module = _load_starter_fresh()
    client = TestClient(module.app)
    resp = client.get("/admin/dashboard")
    assert resp.status_code == 200
    # Test user profile also accessible
    resp2 = client.get("/user/profile")
    assert resp2.status_code == 200
