from typing import Generic, List, Optional, TypeVar

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    message: str


class User(BaseModel):
    id: int
    name: str
    email: str


users_db = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
]


@app.get("/users/")
def get_users():
    return APIResponse[List[User]](success=True, data=users_db, message="Users retrieved")


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        return JSONResponse(
            status_code=404,
            content=APIResponse[User](success=False, data=None, message="User not found").model_dump(),
        )
    return APIResponse[User](success=True, data=user, message="User found")
