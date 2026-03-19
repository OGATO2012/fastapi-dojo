import importlib.util, os
from fastapi.testclient import TestClient


def _load_starter():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_50", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_starter = _load_starter()
client = TestClient(_starter.app)


def test_normal_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert "items" in response.json()


def test_dependency_override():
    def fake_database():
        return {"type": "test", "data": ["test_item_1", "test_item_2"]}

    _starter.app.dependency_overrides[_starter.get_database] = fake_database
    try:
        response = client.get("/items/")
        assert response.status_code == 200
        assert response.json() == {"items": ["test_item_1", "test_item_2"]}

        response2 = client.get("/db-info")
        assert response2.json() == {"db_type": "test"}
    finally:
        _starter.app.dependency_overrides.clear()


def test_no_override():
    response = client.get("/db-info")
    assert response.status_code == 200
    assert response.json() == {"db_type": "production"}
