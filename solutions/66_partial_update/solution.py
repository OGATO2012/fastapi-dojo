from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class UserUpdate(BaseModel):
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


@app.patch("/users/{user_id}")
def partial_update_user(user_id: int, update: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    existing = users[user_id]
    update_data = update.model_dump(exclude_unset=True)
    updated_user = existing.model_copy(update=update_data)
    users[user_id] = updated_user
    return updated_user


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]
