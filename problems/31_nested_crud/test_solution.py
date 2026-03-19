import importlib.util, os, pytest
from fastapi.testclient import TestClient


def _load_starter_fresh():
    path = os.path.join(os.path.dirname(__file__), "starter.py")
    spec = importlib.util.spec_from_file_location("starter_31", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def client():
    module = _load_starter_fresh()
    return TestClient(module.app)


def test_create_department(client):
    response = client.post("/departments/", json={"name": "Engineering"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Engineering"
    assert "id" in data


def test_add_employee(client):
    dept = client.post("/departments/", json={"name": "Engineering"}).json()
    dept_id = dept["id"]
    response = client.post(f"/departments/{dept_id}/employees", json={"name": "Alice", "role": "Engineer"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["role"] == "Engineer"


def test_list_employees(client):
    dept = client.post("/departments/", json={"name": "Engineering"}).json()
    dept_id = dept["id"]
    client.post(f"/departments/{dept_id}/employees", json={"name": "Alice", "role": "Engineer"})
    client.post(f"/departments/{dept_id}/employees", json={"name": "Bob", "role": "Manager"})
    response = client.get(f"/departments/{dept_id}/employees")
    assert response.status_code == 200
    employees = response.json()
    assert len(employees) == 2
    names = [e["name"] for e in employees]
    assert "Alice" in names
    assert "Bob" in names


def test_404_for_unknown_department(client):
    response = client.get("/departments/999/employees")
    assert response.status_code == 404


def test_404_add_employee_to_unknown_department(client):
    response = client.post("/departments/999/employees", json={"name": "Alice", "role": "Engineer"})
    assert response.status_code == 404
