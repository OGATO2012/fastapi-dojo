import importlib.util
import os
import io
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_94_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_upload_basic(client):
    response = client.post(
        "/upload",
        data={"name": "test", "description": "a test file"},
        files={"file": ("hello.txt", b"hello content", "text/plain")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "test"
    assert data["description"] == "a test file"
    assert data["filename"] == "hello.txt"


def test_upload_content_type(client):
    response = client.post(
        "/upload",
        data={"name": "img"},
        files={"file": ("photo.png", b"\x89PNG", "image/png")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["content_type"] == "image/png"


def test_upload_default_description(client):
    response = client.post(
        "/upload",
        data={"name": "nodesc"},
        files={"file": ("data.bin", b"\x00\x01", "application/octet-stream")},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == ""


def test_upload_missing_file(client):
    response = client.post("/upload", data={"name": "nofile"})
    assert response.status_code == 422


def test_upload_missing_name(client):
    response = client.post(
        "/upload",
        files={"file": ("f.txt", b"data", "text/plain")},
    )
    assert response.status_code == 422
