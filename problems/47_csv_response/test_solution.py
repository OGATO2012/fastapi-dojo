import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_47", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_csv_status_code():
    response = client.get("/export/csv")
    assert response.status_code == 200


def test_csv_content_type():
    response = client.get("/export/csv")
    assert "text/csv" in response.headers["content-type"]


def test_csv_body_starts_with_header():
    response = client.get("/export/csv")
    assert response.text.startswith("id,name,price")


def test_csv_content_disposition():
    response = client.get("/export/csv")
    assert "attachment" in response.headers["content-disposition"]
