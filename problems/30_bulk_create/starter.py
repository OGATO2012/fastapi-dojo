from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

items_db: List[dict] = []
next_id = 1

class ItemCreate(BaseModel):
    name: str
    price: float

# TODO: POSTエンドポイント /items/bulk を実装してください
# - List[ItemCreate] を受け取る
# - 各アイテムに自動採番の id を割り当てて保存する
# - status_code=201 を返す
# - レスポンス形式: {"created": [...], "count": N}
#
# TODO: Implement POST /items/bulk endpoint
# - Accept List[ItemCreate]
# - Assign auto-incremented id to each item and store them
# - Return status_code=201
# - Response format: {"created": [...], "count": N}

# TODO: GETエンドポイント /items/ を実装してください
# - 全アイテムのリストを返す
#
# TODO: Implement GET /items/ endpoint
# - Return the list of all stored items
