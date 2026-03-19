from fastapi import Depends, FastAPI

app = FastAPI()


# TODO: `async def get_db()` を実装してください。
# TODO: `{"status": "connected", "host": "localhost"}` を返す非同期依存関数。
# TODO: Implement `async def get_db()`.
# TODO: Async dependency that returns `{"status": "connected", "host": "localhost"}`.


# TODO: `GET /data` エンドポイントを実装してください。
# TODO: `get_db` を Depends で使用し `{"db": "connected", "data": [1, 2, 3]}` を返す。
# TODO: Implement `GET /data`.
# TODO: Use `get_db` via Depends, return `{"db": "connected", "data": [1, 2, 3]}`.


# TODO: `GET /health` エンドポイントを実装してください。
# TODO: `get_db` を Depends で使用し `{"status": "ok", "db_host": "localhost"}` を返す。
# TODO: Implement `GET /health`.
# TODO: Use `get_db` via Depends, return `{"status": "ok", "db_host": "localhost"}`.
