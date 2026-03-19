import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_46", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app, follow_redirects=False)


def test_redirect():
    response = client.get("/old-path")
    assert response.status_code == 301
    assert response.headers["location"].endswith("/new-path")


def test_new_path():
    client2 = TestClient(_starter.app)
    response = client2.get("/new-path")
    assert response.status_code == 200
    assert response.json() == {"message": "You reached the new path"}
