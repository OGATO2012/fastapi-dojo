# Problem 35: Async Endpoints

## Topic
Async Endpoints - Implement async def endpoints

## Task
Create a FastAPI application with two async endpoints:

1. `GET /async-data` - Returns `{"data": "async result", "type": "async"}` using `async def` with `await asyncio.sleep(0)`
2. `GET /async-items/{item_id}` - Returns `{"item_id": item_id, "name": "Item {item_id}"}` using `async def`

## タスク（日本語）
`async def` を使った非同期エンドポイントを実装してください。

## Expected Behavior
- GET /async-data returns {"data": "async result", "type": "async"}
- GET /async-items/5 returns {"item_id": 5, "name": "Item 5"}
