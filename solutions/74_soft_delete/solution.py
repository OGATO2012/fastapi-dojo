from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    is_deleted: bool = False


class ItemCreate(BaseModel):
    name: str


items: dict[int, Item] = {}
next_id = 1


@app.post("/items/")
def create_item(item: ItemCreate):
    global next_id
    new_item = Item(id=next_id, name=item.name)
    items[next_id] = new_item
    next_id += 1
    return new_item


@app.delete("/items/{item_id}")
def soft_delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = items[item_id].model_copy(update={"is_deleted": True})
    return {"message": "Item soft deleted"}


@app.get("/items/deleted")
def get_deleted_items():
    return [item for item in items.values() if item.is_deleted]


@app.get("/items/")
def get_active_items():
    return [item for item in items.values() if not item.is_deleted]
