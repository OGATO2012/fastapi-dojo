import importlib.util, os, pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_52", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_items_endpoint(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": ["a", "b", "c"]}


def test_logs_contain_items_request(client):
    client.get("/items")
    response = client.get("/logs")
    assert response.status_code == 200
    logs = response.json()
    items_logs = [e for e in logs if e["path"] == "/items"]
    assert len(items_logs) >= 1
    assert items_logs[0]["method"] == "GET"


def test_log_entry_has_required_fields(client):
    client.get("/items")
    response = client.get("/logs")
    logs = response.json()
    items_logs = [e for e in logs if e["path"] == "/items"]
    entry = items_logs[0]
    assert "method" in entry
    assert "path" in entry
    assert "status_code" in entry
    assert "duration_ms" in entry
    assert entry["status_code"] == 200
