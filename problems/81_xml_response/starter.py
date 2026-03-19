from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]


# TODO: `GET /users/` エンドポイントを実装してください。
# TODO: 全ユーザーを XML 形式で返す（media_type="application/xml"）。
# TODO: `GET /users/{user_id}` エンドポイントを実装してください。
# TODO: 指定IDのユーザーを XML 形式で返す。存在しない場合は 404。
# TODO: Implement `GET /users/`.
# TODO: Return all users as XML (media_type="application/xml").
# TODO: Implement `GET /users/{user_id}`.
# TODO: Return the user with given ID as XML, or 404 if not found.
