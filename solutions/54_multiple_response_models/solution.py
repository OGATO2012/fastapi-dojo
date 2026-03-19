from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ItemResponse(BaseModel):
    id: int
    name: str
    price: float


class ErrorResponse(BaseModel):
    detail: str
    code: str


ITEMS = {1: {"id": 1, "name": "Apple", "price": 1.5}}


@app.get(
    "/items/{item_id}",
    responses={
        200: {"model": ItemResponse},
        404: {"model": ErrorResponse},
    },
)
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return ITEMS[item_id]
