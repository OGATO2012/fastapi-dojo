import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_68_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "WebSocket server ready"}


def test_websocket_echo(client):
    with client.websocket_connect("/ws") as ws:
        ws.send_text("Hello")
        data = ws.receive_text()
        assert data == "Echo: Hello"


def test_websocket_multiple_messages(client):
    with client.websocket_connect("/ws") as ws:
        ws.send_text("First")
        assert ws.receive_text() == "Echo: First"
        ws.send_text("Second")
        assert ws.receive_text() == "Echo: Second"
