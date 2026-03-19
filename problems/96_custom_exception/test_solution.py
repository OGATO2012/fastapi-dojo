import importlib.util
import os
import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_96_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=False)


def test_unicorn_normal(client):
    response = client.get("/unicorns/sparkle")
    assert response.status_code == 200
    assert response.json() == {"unicorn": "sparkle"}


def test_unicorn_forbidden_status(client):
    response = client.get("/unicorns/forbidden")
    assert response.status_code == 418


def test_unicorn_forbidden_message(client):
    response = client.get("/unicorns/forbidden")
    data = response.json()
    assert data == {"message": "Oops! unicorn forbidden did something."}


def test_unicorn_other_name(client):
    response = client.get("/unicorns/rainbow")
    assert response.status_code == 200
    assert response.json()["unicorn"] == "rainbow"


def test_exception_class_exists():
    module = _load_starter_fresh()
    assert hasattr(module, "UnicornException")
    exc = module.UnicornException(name="test")
    assert exc.name == "test"
