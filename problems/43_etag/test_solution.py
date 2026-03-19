import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_43", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_first_request_returns_200_with_etag():
    response = client.get("/data")
    assert response.status_code == 200
    assert "etag" in response.headers
    assert response.json()["items"] == ["apple", "banana", "cherry"]


def test_conditional_request_returns_304():
    first = client.get("/data")
    etag = first.headers["etag"]
    second = client.get("/data", headers={"If-None-Match": etag})
    assert second.status_code == 304


def test_wrong_etag_returns_200():
    response = client.get("/data", headers={"If-None-Match": '"wrong-etag"'})
    assert response.status_code == 200
    assert "etag" in response.headers
