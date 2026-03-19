# Problem 34: Lifespan Events

## Topic
Lifespan Events - Use lifespan context manager for startup/shutdown

## Task
Create a FastAPI application using the `lifespan` context manager to initialize a fake database on startup and clean it up on shutdown.

On startup, set:
- `fake_db["initialized"] = True`
- `fake_db["items"] = ["apple", "banana", "cherry"]`

Implement `GET /items` which returns:
`{"items": fake_db.get("items", []), "db_initialized": fake_db.get("initialized", False)}`

## タスク（日本語）
`lifespan` コンテキストマネージャーを使ってスタートアップ時にデータを初期化するFastAPIアプリを実装してください。

## Expected Behavior
- After lifespan startup, GET /items returns db_initialized=True and items list with 3 elements
