from typing import Optional

from fastapi import FastAPI

app = FastAPI()

all_items = [{"id": i, "name": f"Item {i}"} for i in range(1, 21)]


# TODO: `GET /items` エンドポイントを実装してください。
# TODO: クエリパラメータ: `cursor: Optional[int] = None`, `limit: int = 10`
# TODO: cursorが指定された場合、id > cursor のアイテムを返す。
# TODO: 返すアイテム数が limit と等しい場合、next_cursor = 最後のアイテムのid。
# TODO: それ以外の場合、next_cursor = None。
# TODO: レスポンス形式: `{"items": [...], "next_cursor": int_or_null}`
# TODO: Implement `GET /items`.
# TODO: Query params: `cursor: Optional[int] = None`, `limit: int = 10`
# TODO: If cursor provided, return items with id > cursor.
# TODO: next_cursor = last item's id if len(returned) == limit, else None.
# TODO: Response format: `{"items": [...], "next_cursor": int_or_null}`
