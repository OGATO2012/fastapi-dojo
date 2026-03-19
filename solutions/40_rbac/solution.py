from fastapi import FastAPI, HTTPException, Header, Depends
from typing import Optional

app = FastAPI()

USERS = {
    "admin-token": {"username": "admin", "role": "admin"},
    "user-token": {"username": "alice", "role": "user"},
}


def get_current_user(x_token: str = Header(...)):
    user = USERS.get(x_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user


def admin_required(x_token: str = Header(...)):
    user = USERS.get(x_token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


@app.get("/me")
def get_me(user: dict = Depends(get_current_user)):
    return user


@app.get("/admin/dashboard")
def admin_dashboard(user: dict = Depends(admin_required)):
    return {"message": "Welcome to admin dashboard", "user": user["username"]}
