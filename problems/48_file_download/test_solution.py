import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_48", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_download_status_code():
    response = client.get("/download/report.txt")
    assert response.status_code == 200


def test_download_content_disposition():
    response = client.get("/download/report.txt")
    assert "attachment" in response.headers["content-disposition"]


def test_download_content_type():
    response = client.get("/download/report.txt")
    assert "text/plain" in response.headers["content-type"]


def test_download_body_not_empty():
    response = client.get("/download/report.txt")
    assert len(response.text) > 0
