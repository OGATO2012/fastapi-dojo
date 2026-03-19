import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_44", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_stream_status_code():
    response = client.get("/stream")
    assert response.status_code == 200


def test_stream_content_type():
    response = client.get("/stream")
    assert "text/plain" in response.headers["content-type"]


def test_stream_body_contains_chunks():
    response = client.get("/stream")
    body = response.text
    for i in range(5):
        assert f"chunk {i}" in body
