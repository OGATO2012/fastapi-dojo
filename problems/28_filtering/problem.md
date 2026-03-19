# Problem 28: Filtering

## Topic
Filtering - Filter items by query parameters

## Task
Create a FastAPI application with a `GET /items/` endpoint that supports optional filtering by `category`.

The dataset:
- Apple (fruit), Banana (fruit), Carrot (vegetable), Broccoli (vegetable)

## タスク（日本語）
`category` クエリパラメータでアイテムをフィルタリングできる `GET /items/` エンドポイントを実装してください。

## Expected Behavior
- No filter returns all 4 items
- `?category=fruit` returns 2 items
- `?category=vegetable` returns 2 items
- Unknown category returns empty list
