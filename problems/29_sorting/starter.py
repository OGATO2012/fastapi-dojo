from fastapi import FastAPI
from typing import Optional

app = FastAPI()

ITEMS = [
    {"id": 3, "name": "Cherry", "price": 3.0},
    {"id": 1, "name": "Apple", "price": 1.5},
    {"id": 2, "name": "Banana", "price": 2.0},
]

# TODO: GETエンドポイント /items/ を実装してください
# - オプショナルなクエリパラメータ: sort_by (デフォルト=None), order (デフォルト="asc")
# - sort_by が "id", "name", "price" のいずれかの場合にソートを適用する
# - order="desc" の場合は降順でソートする
# - ソートフィールドが指定されない場合は元の順序を返す
#
# TODO: Implement GET /items/ endpoint
# - Optional query parameters: sort_by (default=None), order (default="asc")
# - Apply sorting if sort_by is one of: "id", "name", "price"
# - Sort in descending order if order="desc"
# - Return original order if no sort_by is specified
