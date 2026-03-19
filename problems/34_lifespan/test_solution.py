import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_34", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_lifespan_items():
    starter = _load_starter()
    with TestClient(starter.app) as client:
        response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert data["db_initialized"] is True
    assert len(data["items"]) > 0
