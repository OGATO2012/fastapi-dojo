# Problem 75: Cursor Pagination

## 概要 / Overview

カーソルベースのページネーションを実装してください。
Implement cursor-based pagination.

## 要件 / Requirements

1. 20件のアイテムをプリロード: `[{"id": i, "name": f"Item {i}"} for i in range(1, 21)]` / 20 pre-loaded items
2. `GET /items` (クエリパラメータ: `cursor: Optional[int] = None`, `limit: int = 10`) / Query params: cursor and limit
3. レスポンス: `{"items": [...], "next_cursor": int_or_null}` / Response format
4. cursorが指定された場合、id > cursor のアイテムを返す / If cursor provided, return items with id > cursor
5. それ以上アイテムがない場合、next_cursorはnull / If no more items, next_cursor is null

## 期待される動作 / Expected Behavior

- カーソルは最後に見たアイテムのidを表す / Cursor represents the id of the last item seen
- `next_cursor` = 返したアイテムの最後のid (limitと同数の場合)、それ以外は null / next_cursor = last item's id if len == limit, else None
- カーソルなしでは最初のlimit件を返す / Without cursor, returns first `limit` items
