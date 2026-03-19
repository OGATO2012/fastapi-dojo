from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

FAKE_DB = {
    "users": {
        1: {"id": 1, "username": "alice", "is_admin": True},
        2: {"id": 2, "username": "bob", "is_admin": False},
    }
}


def get_db():
    return FAKE_DB


def get_current_user(db: dict = Depends(get_db)):
    return db["users"][1]


def get_admin_user(user: dict = Depends(get_current_user)):
    if not user["is_admin"]:
        raise HTTPException(status_code=403, detail="Not an admin")
    return user


@app.get("/admin/dashboard")
async def admin_dashboard(user: dict = Depends(get_admin_user)):
    return {"dashboard": "admin data", "user": user["username"]}


@app.get("/user/profile")
async def user_profile(user: dict = Depends(get_current_user)):
    return {"profile": user}
