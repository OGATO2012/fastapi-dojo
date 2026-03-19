import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_53", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_openapi_status_code():
    response = client.get("/openapi.json")
    assert response.status_code == 200


def test_openapi_custom_title():
    response = client.get("/openapi.json")
    assert response.json()["info"]["title"] == "My Awesome API"


def test_openapi_custom_version():
    response = client.get("/openapi.json")
    assert response.json()["info"]["version"] == "2.0.0"


def test_openapi_description_has_markdown():
    response = client.get("/openapi.json")
    description = response.json()["info"].get("description", "")
    assert "**" in description


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
