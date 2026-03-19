import importlib.util
import io
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_70_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_upload_single_file(client):
    files = [("files", ("test.txt", io.BytesIO(b"Hello"), "text/plain"))]
    response = client.post("/upload/multiple", files=files)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["filename"] == "test.txt"
    assert data[0]["size"] == 5


def test_upload_multiple_files(client):
    files = [
        ("files", ("file1.txt", io.BytesIO(b"Hello"), "text/plain")),
        ("files", ("file2.txt", io.BytesIO(b"World!"), "text/plain")),
    ]
    response = client.post("/upload/multiple", files=files)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    filenames = [f["filename"] for f in data]
    assert "file1.txt" in filenames
    assert "file2.txt" in filenames


def test_upload_empty_list(client):
    response = client.post("/upload/multiple")
    assert response.status_code == 422
