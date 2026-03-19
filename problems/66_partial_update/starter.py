from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class UserUpdate(BaseModel):
    # TODO: 全フィールドをOptionalにしてください / Make all fields Optional
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


users: dict[int, User] = {
    1: User(id=1, name="Alice", email="alice@example.com", age=30)
}


# TODO: `PATCH /users/{user_id}` を実装してください。
# TODO: `.model_dump(exclude_unset=True)` を使って提供されたフィールドのみを更新する。
# TODO: Implement `PATCH /users/{user_id}`.
# TODO: Use `.model_dump(exclude_unset=True)` to only update provided fields.


# TODO: `GET /users/{user_id}` を実装してください。存在しない場合は 404。
# TODO: Implement `GET /users/{user_id}`. Return 404 if not found.
