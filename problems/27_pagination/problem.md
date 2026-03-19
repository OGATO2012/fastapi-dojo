# Problem 27: Pagination

## Topic
Pagination - Implement offset-based pagination on a fixed list

## Task
Create a FastAPI application with a `GET /items/` endpoint that supports pagination via `skip` and `limit` query parameters.

- The dataset contains 100 items with id 1-100
- Default: skip=0, limit=10
- Response format: `{"items": [...], "total": 100, "skip": skip, "limit": limit}`

## タスク（日本語）
`skip` と `limit` クエリパラメータを使ったページネーションをサポートする `GET /items/` エンドポイントを実装してください。

## Expected Behavior
- `GET /items/` returns 10 items by default
- `GET /items/?skip=0&limit=5` returns 5 items
- `GET /items/?skip=10&limit=5` returns 5 items starting at Item 11
