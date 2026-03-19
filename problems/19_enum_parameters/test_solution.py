import importlib.util
import os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_19", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_alexnet_returns_message():
    response = client.get("/models/alexnet")
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "alexnet"
    assert "Deep Learning FTW!" in data["message"]


def test_resnet_returns_message():
    response = client.get("/models/resnet")
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "resnet"
    assert "residuals" in data["message"]


def test_lenet_returns_message():
    response = client.get("/models/lenet")
    assert response.status_code == 200
    data = response.json()
    assert data["model_name"] == "lenet"
    assert "LeCNN" in data["message"]


def test_invalid_model_returns_422():
    response = client.get("/models/invalid_model")
    assert response.status_code == 422
