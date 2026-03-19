import importlib.util, os, pytest
from fastapi.testclient import TestClient

def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_61", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_default_settings():
    module = _load_starter_fresh()
    client = TestClient(module.app)
    response = client.get("/settings")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "debug" in data
    assert "api_version" in data

def test_settings_have_expected_fields():
    module = _load_starter_fresh()
    client = TestClient(module.app)
    response = client.get("/settings")
    data = response.json()
    assert data["debug"] == False
    assert data["max_items"] == 100
