import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_45", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_html_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_html_content_type():
    response = client.get("/")
    assert "text/html" in response.headers["content-type"]


def test_html_body_contains_greeting():
    response = client.get("/")
    assert "Hello from FastAPI!" in response.text
