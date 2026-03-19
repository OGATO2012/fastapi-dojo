from fastapi import FastAPI, Cookie, Response, HTTPException
from typing import Optional

app = FastAPI()

FAKE_USERS = {"user123": {"username": "alice", "email": "alice@example.com"}}
SESSION_TOKEN = "session_abc123"

# TODO: POST /login エンドポイントを実装してください
# レスポンスに "session" クッキーを設定する (値: SESSION_TOKEN)
# {"message": "logged in"} を返す
# TODO: Implement POST /login
# Set "session" cookie in response (value: SESSION_TOKEN)
# Return {"message": "logged in"}

# TODO: GET /profile エンドポイントを実装してください
# "session" クッキーを読み取り, SESSION_TOKEN と一致すれば FAKE_USERS["user123"] を返す
# 一致しなければ HTTP 401 を返す
# TODO: Implement GET /profile
# Read "session" cookie, return FAKE_USERS["user123"] if matches SESSION_TOKEN
# Return HTTP 401 if no valid session

# TODO: POST /logout エンドポイントを実装してください
# "session" クッキーを削除して {"message": "logged out"} を返す
# TODO: Implement POST /logout
# Delete "session" cookie and return {"message": "logged out"}
