from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordRequest(BaseModel):
    password: str


class VerifyRequest(BaseModel):
    password: str
    hashed_password: str


@app.post("/hash-password")
def hash_password(req: PasswordRequest):
    hashed = pwd_context.hash(req.password)
    return {"hashed_password": hashed}


@app.post("/verify-password")
def verify_password(req: VerifyRequest):
    is_valid = pwd_context.verify(req.password, req.hashed_password)
    return {"is_valid": is_valid}
