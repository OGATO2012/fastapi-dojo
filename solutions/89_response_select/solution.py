from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

USERS = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com", "password": "secret1", "age": 30},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com", "password": "secret2", "age": 25},
}


class UserFull(BaseModel):
    id: int
    name: str
    email: str
    password: str
    age: int


class UserPublic(BaseModel):
    id: int
    name: str
    email: str
    age: int


@app.get("/users/{user_id}")
async def read_user(user_id: int, fields: Optional[str] = Query(default=None)):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    user = USERS[user_id]
    if fields:
        field_list = [f.strip() for f in fields.split(",")]
        return {k: v for k, v in user.items() if k in field_list}
    return user


@app.get("/users/{user_id}/public", response_model=UserPublic)
async def read_user_public(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]
