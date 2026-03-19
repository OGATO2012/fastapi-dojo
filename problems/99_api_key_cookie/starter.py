from fastapi import FastAPI, Cookie, Response, HTTPException, Query
from typing import Optional

app = FastAPI()

SECRET_API_KEY = "secret"
AUTH_COOKIE_NAME = "auth_token"
AUTH_COOKIE_VALUE = "authenticated_user_token"

# TODO: POST /auth/login エンドポイントを実装してください
# クエリパラメータ api_key: str を受け取る
# api_key が SECRET_API_KEY と一致すれば AUTH_COOKIE_NAME クッキーを設定
# 一致しなければ HTTP 401 を返す
# TODO: Implement POST /auth/login
# Accept query param api_key: str
# Set AUTH_COOKIE_NAME cookie if api_key matches SECRET_API_KEY
# Return HTTP 401 if not

# TODO: GET /auth/protected エンドポイントを実装してください
# AUTH_COOKIE_NAME クッキーを読み取り, 有効なら {"user": "authenticated", "message": "access granted"} を返す
# 無効なら HTTP 401 を返す
# TODO: Implement GET /auth/protected
# Read AUTH_COOKIE_NAME cookie, return user data if valid
# Return HTTP 401 if invalid or missing

# TODO: POST /auth/logout エンドポイントを実装してください
# AUTH_COOKIE_NAME クッキーを削除して {"message": "logged out"} を返す
# TODO: Implement POST /auth/logout
# Delete AUTH_COOKIE_NAME cookie and return {"message": "logged out"}
