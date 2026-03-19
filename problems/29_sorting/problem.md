# Problem 29: Sorting

## Topic
Sorting - Sort items by field and order

## Task
Create a FastAPI application with a `GET /items/` endpoint that supports sorting via `sort_by` and `order` query parameters.

Dataset:
- Cherry (price: 3.0), Apple (price: 1.5), Banana (price: 2.0)

Supported sort fields: "id", "name", "price"
Order: "asc" (default) or "desc"

## タスク（日本語）
`sort_by` と `order` クエリパラメータでアイテムをソートできる `GET /items/` エンドポイントを実装してください。

## Expected Behavior
- No sort returns original order (Cherry first)
- `?sort_by=name&order=asc` returns [Apple, Banana, Cherry]
- `?sort_by=price&order=desc` returns [Cherry(3.0), Banana(2.0), Apple(1.5)]
