from fastapi import FastAPI
from contextlib import asynccontextmanager

fake_db = {}

# TODO: lifespanコンテキストマネージャーを実装してください
# - スタートアップ時: fake_db["initialized"] = True, fake_db["items"] = ["apple", "banana", "cherry"] を設定
# - yield でアプリを実行
# - シャットダウン時: fake_db.clear() を呼び出す
#
# TODO: Implement the lifespan context manager
# - On startup: set fake_db["initialized"] = True, fake_db["items"] = ["apple", "banana", "cherry"]
# - yield to run the app
# - On shutdown: call fake_db.clear()

# TODO: lifespan を引数に FastAPI アプリを作成してください
# TODO: Create FastAPI app with the lifespan parameter

app = FastAPI()

# TODO: GETエンドポイント /items を実装してください
# - {"items": fake_db.get("items", []), "db_initialized": fake_db.get("initialized", False)} を返す
#
# TODO: Implement GET /items endpoint
# - Return {"items": fake_db.get("items", []), "db_initialized": fake_db.get("initialized", False)}
