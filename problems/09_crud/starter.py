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


# TODO: `GET /items` を実装してください。全アイテムのリストを返す。
# TODO: Implement `GET /items` — return a list of all items.


# TODO: `POST /items` を実装してください。アイテムを作成し id を採番して返す (status 201)。
# TODO: Implement `POST /items` — create an item with an auto-assigned id (status 201).


# TODO: `GET /items/{item_id}` を実装してください。存在しない場合は 404。
# TODO: Implement `GET /items/{item_id}` — return 404 if not found.


# TODO: `PUT /items/{item_id}` を実装してください。アイテムを更新して返す。存在しない場合は 404。
# TODO: Implement `PUT /items/{item_id}` — update item and return it. Return 404 if not found.


# TODO: `DELETE /items/{item_id}` を実装してください。削除してボディなし (status 204)。存在しない場合は 404。
# TODO: Implement `DELETE /items/{item_id}` — delete item, return no body (status 204). Return 404 if not found.
