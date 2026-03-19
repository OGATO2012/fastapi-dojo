from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class ItemCreate(BaseModel):
    name: str


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    return {"name": item.name, "id": 1}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
