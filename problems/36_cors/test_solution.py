import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_36", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {"data": "CORS-enabled response"}


def test_cors_preflight():
    response = client.options(
        "/data",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers


def test_cors_header_on_get():
    response = client.get("/data", headers={"Origin": "http://localhost:3000"})
    assert "access-control-allow-origin" in response.headers
