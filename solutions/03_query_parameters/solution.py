from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, keyword: Optional[str] = None):
    return {"skip": skip, "limit": limit, "keyword": keyword}
