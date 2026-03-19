import importlib.util, os, pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_41", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_first_five_requests_succeed(client):
    for i in range(5):
        response = client.get("/data")
        assert response.status_code == 200, f"Request {i+1} should succeed"
        assert response.json() == {"data": "ok"}


def test_sixth_request_rate_limited(client):
    for _ in range(5):
        client.get("/data")
    response = client.get("/data")
    assert response.status_code == 429
    assert response.json() == {"detail": "Rate limit exceeded"}
