from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "test-secret-key"
ALGORITHM = "HS256"


class TokenRequest(BaseModel):
    username: str


class TokenVerify(BaseModel):
    token: str


@app.post("/create-token")
def create_token(req: TokenRequest):
    payload = {
        "sub": req.username,
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/verify-token")
def verify_token(req: TokenVerify):
    try:
        payload = jwt.decode(req.token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"valid": True, "username": payload["sub"]}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
