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

# TODO: POSTエンドポイント /departments/ を実装してください
# - DepartmentCreate を受け取る
# - 自動採番の id と空の employees リストで部署を作成する
# - status_code=201 を返す
#
# TODO: Implement POST /departments/ endpoint
# - Accept DepartmentCreate
# - Create department with auto-incremented id and empty employees list
# - Return status_code=201

# TODO: POSTエンドポイント /departments/{dept_id}/employees を実装してください
# - dept_id が存在しない場合は 404 を返す
# - EmployeeCreate を受け取り、部署の employees リストに追加する
# - status_code=201 を返す
#
# TODO: Implement POST /departments/{dept_id}/employees endpoint
# - Return 404 if dept_id does not exist
# - Accept EmployeeCreate and append to the department's employees list
# - Return status_code=201

# TODO: GETエンドポイント /departments/{dept_id}/employees を実装してください
# - dept_id が存在しない場合は 404 を返す
# - 部署の従業員リストを返す
#
# TODO: Implement GET /departments/{dept_id}/employees endpoint
# - Return 404 if dept_id does not exist
# - Return the department's employee list
