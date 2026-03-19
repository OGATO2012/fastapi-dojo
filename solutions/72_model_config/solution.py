from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()


class UserStrict(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, str_min_length=1)
    name: str
    email: str


class UserFrozen(BaseModel):
    model_config = ConfigDict(frozen=True)
    name: str
    email: str


@app.post("/users/strict")
def create_strict_user(user: UserStrict):
    return user


@app.post("/users/frozen")
def create_frozen_user(user: UserFrozen):
    return user
