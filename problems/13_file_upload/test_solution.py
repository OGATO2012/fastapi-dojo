import importlib.util
import os
import io
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_13", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_upload_file_returns_filename_and_size():
    content = b"Hello, World!"
    file = io.BytesIO(content)
    response = client.post("/upload", files={"file": ("test.txt", file, "text/plain")})
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "test.txt"
    assert data["size"] == len(content)


def test_upload_file_different_content():
    content = b"FastAPI is awesome!"
    file = io.BytesIO(content)
    response = client.post("/upload", files={"file": ("sample.txt", file, "text/plain")})
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "sample.txt"
    assert data["size"] == len(content)
