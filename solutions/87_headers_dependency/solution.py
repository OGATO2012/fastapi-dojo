from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Optional

app = FastAPI()


async def common_headers(
    x_token: str = Header(...),
    accept_language: str = Header(default="en"),
):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return {"x_token": x_token, "accept_language": accept_language}


@app.get("/items")
async def read_items(headers: dict = Depends(common_headers)):
    return {"items": ["item1", "item2"], "language": headers["accept_language"]}


@app.get("/users")
async def read_users(headers: dict = Depends(common_headers)):
    return {"users": ["alice", "bob"], "language": headers["accept_language"]}
