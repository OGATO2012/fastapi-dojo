from fastapi import FastAPI, Cookie, Response, HTTPException
from typing import Optional

app = FastAPI()

FAKE_USERS = {"user123": {"username": "alice", "email": "alice@example.com"}}
SESSION_TOKEN = "session_abc123"


@app.post("/login")
async def login(response: Response):
    response.set_cookie(key="session", value=SESSION_TOKEN)
    return {"message": "logged in"}


@app.get("/profile")
async def profile(session: Optional[str] = Cookie(default=None)):
    if session != SESSION_TOKEN:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return FAKE_USERS["user123"]


@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="session")
    return {"message": "logged out"}
