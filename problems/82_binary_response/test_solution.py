import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_82_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_placeholder_image(client):
    response = client.get("/image/placeholder")
    assert response.status_code == 200
    assert "image/png" in response.headers["content-type"]
    assert response.content[:8] == b"\x89PNG\r\n\x1a\n"


def test_get_file_txt(client):
    response = client.get("/file/hello.txt")
    assert response.status_code == 200
    assert response.content == b"Hello, World!"


def test_get_file_bin(client):
    response = client.get("/file/data.bin")
    assert response.status_code == 200
    assert response.content == b"\x00\x01\x02\x03"


def test_get_file_not_found(client):
    response = client.get("/file/unknown.txt")
    assert response.status_code == 404
