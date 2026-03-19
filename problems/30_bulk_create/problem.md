# Problem 30: Bulk Create

## Topic
Bulk Create - Create multiple items in one request

## Task
Create a FastAPI application with:
1. `POST /items/bulk` - Accept a list of items and create them all at once (status_code=201)
2. `GET /items/` - Return all stored items

Each item has `name` (str) and `price` (float). Created items get auto-assigned `id` values.

Response from bulk create: `{"created": [...], "count": N}`

## タスク（日本語）
複数のアイテムを一度に作成できるバルク作成エンドポイントを実装してください。

## Expected Behavior
- POST /items/bulk with 2 items returns count=2 and created list with ids
- GET /items/ returns the created items
