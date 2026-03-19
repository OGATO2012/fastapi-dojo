import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_95_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_admin_stats(client):
    response = client.get("/admin/stats")
    assert response.status_code == 200
    assert "stats" in response.json()


def test_admin_cache_delete(client):
    response = client.delete("/admin/cache")
    assert response.status_code == 200
    assert response.json() == {"message": "cache cleared"}


def test_public_info(client):
    response = client.get("/public/info")
    assert response.status_code == 200
    assert response.json() == {"info": "public info"}


def test_public_status(client):
    response = client.get("/public/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_openapi_has_admin_tag(client):
    response = client.get("/openapi.json")
    schema = response.json()
    paths = schema.get("paths", {})
    assert "/admin/stats" in paths


def test_openapi_has_public_tag(client):
    response = client.get("/openapi.json")
    schema = response.json()
    paths = schema.get("paths", {})
    assert "/public/info" in paths


def test_wrong_prefix_not_found(client):
    assert client.get("/stats").status_code == 404
    assert client.get("/info").status_code == 404
