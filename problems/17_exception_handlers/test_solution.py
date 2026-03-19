import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_17", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app, raise_server_exceptions=False)


def test_normal_unicorn_returns_message():
    response = client.get("/unicorns/bob")
    assert response.status_code == 200
    data = response.json()
    assert "bob" in str(data).lower() or "unicorn" in str(data).lower()


def test_yolo_raises_custom_exception():
    response = client.get("/unicorns/yolo")
    assert response.status_code == 418


def test_yolo_returns_error_message():
    response = client.get("/unicorns/yolo")
    data = response.json()
    assert "error" in data
    assert "yolo" in data["error"]
