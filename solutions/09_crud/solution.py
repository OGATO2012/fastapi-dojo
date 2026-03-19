from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = ""


class ItemOut(BaseModel):
    id: int
    name: str
    description: str


items_db: dict[int, ItemOut] = {}
next_id = 1
# NOTE: Using a module-level dict + integer counter is fine for this exercise.
# In production, use a real database (e.g., SQLAlchemy + PostgreSQL) and let the
# database handle ID generation. Multiple workers would otherwise get duplicate IDs.


@app.get("/items", response_model=list[ItemOut])
def list_items():
    return list(items_db.values())


@app.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    global next_id
    new_item = ItemOut(id=next_id, name=item.name, description=item.description)
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = ItemOut(id=item_id, name=item.name, description=item.description)
    items_db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None
