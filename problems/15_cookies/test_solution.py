import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_15", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_set_cookie_returns_message():
    response = client.get("/set-cookie")
    assert response.status_code == 200
    assert response.json() == {"message": "Cookie set"}


def test_set_cookie_sets_header():
    response = client.get("/set-cookie")
    assert "set-cookie" in response.headers


def test_read_cookie_returns_session():
    response = client.get("/read-cookie", cookies={"session": "abc123"})
    assert response.status_code == 200
    assert response.json() == {"session": "abc123"}


def test_read_cookie_no_cookie():
    fresh_client = TestClient(_starter.app)
    response = fresh_client.get("/read-cookie")
    assert response.status_code == 200
    assert response.json() == {"session": None}
