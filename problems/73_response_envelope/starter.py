from typing import Generic, List, Optional, TypeVar

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

T = TypeVar("T")


# TODO: `APIResponse[T]` ジェネリックモデルを実装してください。
# TODO: `success: bool`, `data: Optional[T]`, `message: str` フィールドを持つ。
# TODO: Implement generic `APIResponse[T]` model.
# TODO: Fields: `success: bool`, `data: Optional[T]`, `message: str`.
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


# TODO: `GET /users/` エンドポイントを実装してください。
# TODO: `APIResponse[List[User]]` でラップして返す (success=True, message="Users retrieved")。
# TODO: Implement `GET /users/`.
# TODO: Return wrapped with `APIResponse[List[User]]` (success=True, message="Users retrieved").


# TODO: `GET /users/{user_id}` エンドポイントを実装してください。
# TODO: `APIResponse[User]` でラップして返す (success=True, message="User found")。
# TODO: ユーザーが見つからない場合は success=False, message="User not found", status 404。
# TODO: Implement `GET /users/{user_id}`.
# TODO: Return wrapped with `APIResponse[User]` (success=True, message="User found").
# TODO: If not found: success=False, message="User not found", status 404.
