import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_32", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_search_api_returns_three():
    response = client.get("/search?q=api")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 3
    assert data["query"] == "api"


def test_search_python_returns_one():
    response = client.get("/search?q=python")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 1
    assert data["results"][0]["name"] == "Python Tutorial"


def test_search_no_results():
    response = client.get("/search?q=xyz")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 0
    assert data["results"] == []


def test_search_case_insensitive():
    response = client.get("/search?q=FASTAPI")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] >= 1
