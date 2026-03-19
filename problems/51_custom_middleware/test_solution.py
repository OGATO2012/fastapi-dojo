import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_51", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_custom_middleware_header_present():
    response = client.get("/")
    assert "x-custom-middleware" in response.headers


def test_custom_middleware_header_value():
    response = client.get("/")
    assert response.headers["x-custom-middleware"] == "active"


def test_root_body():
    response = client.get("/")
    assert response.json() == {"message": "Hello"}
