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


# TODO: `POST /items/` エンドポイントを実装してください。アイテムを作成してidを採番し返す。
# TODO: Implement `POST /items/` — create item with auto-assigned id and return it.


# TODO: `DELETE /items/{item_id}` エンドポイントを実装してください。
# TODO: `is_deleted=True` に設定してソフトデリートする。`{"message": "Item soft deleted"}` を返す。
# TODO: 存在しない場合は 404。
# TODO: Implement `DELETE /items/{item_id}` — set is_deleted=True (soft delete).
# TODO: Return `{"message": "Item soft deleted"}`. Return 404 if not found.


# TODO: `GET /items/` エンドポイントを実装してください。削除されていないアイテムのみ返す。
# TODO: Implement `GET /items/` — return only non-deleted items.


# TODO: `GET /items/deleted` エンドポイントを実装してください。削除されたアイテムのみ返す。
# TODO: Implement `GET /items/deleted` — return only deleted items.
