from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

items_db: List[dict] = []
next_id = 1


class ItemCreate(BaseModel):
    name: str
    price: float


@app.post("/items/bulk", status_code=201)
def bulk_create(items: List[ItemCreate]):
    global next_id
    created = []
    for item in items:
        new_item = {"id": next_id, "name": item.name, "price": item.price}
        items_db.append(new_item)
        next_id += 1
        created.append(new_item)
    return {"created": created, "count": len(created)}


@app.get("/items/")
def list_items():
    return items_db
