from fastapi import FastAPI
from typing import List

app = FastAPI()

ITEMS = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]


@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"items": ITEMS[skip: skip + limit], "total": len(ITEMS), "skip": skip, "limit": limit}
