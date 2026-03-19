from fastapi import FastAPI
from typing import List

app = FastAPI()

ITEMS = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]

# TODO: GETエンドポイント /items/ を実装してください
# - クエリパラメータ: skip (デフォルト=0), limit (デフォルト=10)
# - ITEMS リストをスライスして返す
# - レスポンス形式: {"items": [...], "total": 100, "skip": skip, "limit": limit}
#
# TODO: Implement GET /items/ endpoint
# - Query parameters: skip (default=0), limit (default=10)
# - Slice the ITEMS list and return paginated results
# - Response format: {"items": [...], "total": 100, "skip": skip, "limit": limit}
