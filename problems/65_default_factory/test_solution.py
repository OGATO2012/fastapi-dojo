import importlib.util, os
from fastapi.testclient import TestClient

def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_65", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

_starter = _load_starter()
client = TestClient(_starter.app)

def test_create_todo_auto_id():
    response = client.post("/todos/", json={"title": "Buy groceries"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert len(data["id"]) > 0
    assert data["tags"] == []
    assert "created_at" in data

def test_create_todo_unique_ids():
    r1 = client.post("/todos/", json={"title": "Task 1"})
    r2 = client.post("/todos/", json={"title": "Task 2"})
    assert r1.json()["id"] != r2.json()["id"]

def test_minimal_todo():
    response = client.post("/todos/minimal?title=Simple+Task")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Simple Task"
    assert data["tags"] == []
