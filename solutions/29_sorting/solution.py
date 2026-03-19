from fastapi import FastAPI
from typing import Optional

app = FastAPI()

ITEMS = [
    {"id": 3, "name": "Cherry", "price": 3.0},
    {"id": 1, "name": "Apple", "price": 1.5},
    {"id": 2, "name": "Banana", "price": 2.0},
]


@app.get("/items/")
def get_items(sort_by: Optional[str] = None, order: str = "asc"):
    items = ITEMS.copy()
    if sort_by and sort_by in ("id", "name", "price"):
        items = sorted(items, key=lambda x: x[sort_by], reverse=(order == "desc"))
    return items
