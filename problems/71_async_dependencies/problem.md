# Problem 71: Async Dependencies

## 概要 / Overview

非同期依存性注入を実装してください。
Implement async dependency injection.

## 要件 / Requirements

1. `async def get_db()` - `{"status": "connected", "host": "localhost"}` を返す非同期依存関数 / Async dependency returning `{"status": "connected", "host": "localhost"}`
2. `GET /data` - `get_db` 依存関係を使い `{"db": "connected", "data": [1, 2, 3]}` を返す / Uses `get_db`, returns `{"db": "connected", "data": [1, 2, 3]}`
3. `GET /health` - `get_db` 依存関係を使い `{"status": "ok", "db_host": "localhost"}` を返す / Uses `get_db`, returns `{"status": "ok", "db_host": "localhost"}`

## 期待される動作 / Expected Behavior

- `async def` で定義された依存関数が正しく動作する / Async dependency function works correctly
- 各エンドポイントが依存関係から取得したDB情報を使用する / Each endpoint uses DB info from dependency
