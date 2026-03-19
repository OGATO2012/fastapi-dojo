from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

departments: Dict[int, dict] = {}
dept_counter = 1


class DepartmentCreate(BaseModel):
    name: str


class EmployeeCreate(BaseModel):
    name: str
    role: str


@app.post("/departments/", status_code=201)
def create_department(dept: DepartmentCreate):
    global dept_counter
    new_dept = {"id": dept_counter, "name": dept.name, "employees": []}
    departments[dept_counter] = new_dept
    dept_counter += 1
    return new_dept


@app.post("/departments/{dept_id}/employees", status_code=201)
def add_employee(dept_id: int, emp: EmployeeCreate):
    if dept_id not in departments:
        raise HTTPException(status_code=404, detail="Department not found")
    emp_data = {"name": emp.name, "role": emp.role}
    departments[dept_id]["employees"].append(emp_data)
    return emp_data


@app.get("/departments/{dept_id}/employees")
def list_employees(dept_id: int):
    if dept_id not in departments:
        raise HTTPException(status_code=404, detail="Department not found")
    return departments[dept_id]["employees"]
