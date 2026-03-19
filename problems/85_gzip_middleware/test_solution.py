import importlib.util
import os

import pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_85_fresh", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app, raise_server_exceptions=True)


def test_large_data_returns_100_items(client):
    response = client.get("/large-data")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100


def test_large_data_item_shape(client):
    response = client.get("/large-data")
    item = response.json()[0]
    assert "id" in item
    assert "name" in item
    assert "value" in item


def test_small_data(client):
    response = client.get("/small-data")
    assert response.status_code == 200
    assert response.json() == {"message": "small"}


def test_large_data_compressed():
    module = _load_starter_fresh()
    c = TestClient(module.app, raise_server_exceptions=True)
    response = c.get("/large-data", headers={"Accept-Encoding": "gzip"})
    assert response.status_code == 200
    assert response.headers.get("content-encoding") == "gzip"


def test_small_data_not_compressed():
    module = _load_starter_fresh()
    c = TestClient(module.app, raise_server_exceptions=True)
    response = c.get("/small-data", headers={"Accept-Encoding": "gzip"})
    assert response.status_code == 200
    assert response.headers.get("content-encoding") != "gzip"
