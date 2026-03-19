# Problem 31: Nested CRUD

## Topic
Nested CRUD - CRUD for a parent resource with child items

## Task
Create a FastAPI application managing departments and their employees:

1. `POST /departments/` - Create a department (status_code=201)
2. `POST /departments/{dept_id}/employees` - Add an employee to a department (status_code=201)
3. `GET /departments/{dept_id}/employees` - List employees of a department

Department has `name`. Employee has `name` and `role`. Return 404 if department not found.

## タスク（日本語）
部署と従業員のネストされたCRUDを実装してください。

## Expected Behavior
- Create department, add employees, list employees returns them
- 404 for unknown department id
