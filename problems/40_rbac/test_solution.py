import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_40", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app, raise_server_exceptions=False)


def test_me_admin():
    response = client.get("/me", headers={"X-Token": "admin-token"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"
    assert data["role"] == "admin"


def test_me_user():
    response = client.get("/me", headers={"X-Token": "user-token"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["role"] == "user"


def test_admin_dashboard_success():
    response = client.get("/admin/dashboard", headers={"X-Token": "admin-token"})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_admin_dashboard_user_forbidden():
    response = client.get("/admin/dashboard", headers={"X-Token": "user-token"})
    assert response.status_code == 403


def test_admin_dashboard_no_token():
    response = client.get("/admin/dashboard")
    assert response.status_code == 422
