import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_42", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_cached_data_header():
    response = client.get("/cached-data")
    assert response.status_code == 200
    assert "max-age=3600" in response.headers["cache-control"]
    assert "public" in response.headers["cache-control"]


def test_no_cache_data_header():
    response = client.get("/no-cache-data")
    assert response.status_code == 200
    assert "no-store" in response.headers["cache-control"]


def test_cached_data_body():
    response = client.get("/cached-data")
    assert "data" in response.json()


def test_no_cache_data_body():
    response = client.get("/no-cache-data")
    assert "data" in response.json()
