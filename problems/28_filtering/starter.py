from fastapi import FastAPI
from typing import Optional, List

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "Apple", "category": "fruit"},
    {"id": 2, "name": "Banana", "category": "fruit"},
    {"id": 3, "name": "Carrot", "category": "vegetable"},
    {"id": 4, "name": "Broccoli", "category": "vegetable"},
]

# TODO: GETエンドポイント /items/ を実装してください
# - オプショナルなクエリパラメータ: category (デフォルト=None)
# - category が指定された場合、その category のアイテムのみ返す
# - category が指定されない場合、全アイテムを返す
#
# TODO: Implement GET /items/ endpoint
# - Optional query parameter: category (default=None)
# - If category is provided, return only items matching that category
# - If no category, return all items
