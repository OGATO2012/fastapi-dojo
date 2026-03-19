from typing import Optional

from fastapi import FastAPI

app = FastAPI()

all_items = [{"id": i, "name": f"Item {i}"} for i in range(1, 21)]


# TODO: `GET /items` エンドポイントを実装してください。
# TODO: クエリパラメータ: `cursor: Optional[int] = None`, `limit: int = 10`
# TODO: cursorが指定された場合、id > cursor のアイテムを返す。
# TODO: limit+1 件取得して次のページが存在するか判定する。次ページあり → next_cursor = ページ最後のid、なし → None。
# TODO: レスポンス形式: `{"items": [...], "next_cursor": int_or_null}`
# TODO: Implement `GET /items`.
# TODO: Query params: `cursor: Optional[int] = None`, `limit: int = 10`
# TODO: If cursor provided, return items with id > cursor.
# TODO: Fetch limit+1 items to detect if more exist. If more: next_cursor = last item's id. Otherwise: None.
# TODO: Response format: `{"items": [...], "next_cursor": int_or_null}`
