from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()


class Item(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    item_id: int = Field(..., alias="id")
    item_name: str = Field(..., alias="name")


@app.post("/items")
def create_item(item: Item):
    return {"item_id": item.item_id, "item_name": item.item_name}
