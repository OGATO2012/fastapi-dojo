import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_12", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_send_notification_returns_status():
    response = client.post("/send-notification", json={"message": "hello"})
    assert response.status_code == 200
    assert response.json() == {"status": "Message sent"}


def test_send_notification_with_different_message():
    response = client.post("/send-notification", json={"message": "test message"})
    assert response.status_code == 200
    assert response.json()["status"] == "Message sent"


def test_send_notification_requires_message():
    response = client.post("/send-notification", json={})
    assert response.status_code == 422
