from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, Set

app = FastAPI()

USERS = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com", "password": "secret1", "age": 30},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com", "password": "secret2", "age": 25},
}


class UserFull(BaseModel):
    id: int
    name: str
    email: str
    password: str
    age: int


class UserPublic(BaseModel):
    id: int
    name: str
    email: str
    age: int


# TODO: GET /users/{user_id} エンドポイントを実装してください
# クエリパラメータ fields (カンマ区切り) で返すフィールドを絞り込む
# 例: ?fields=name,email → {"name": "Alice", "email": "alice@example.com"}
# fields が未指定の場合は全フィールドを返す (パスワードも含む)
# TODO: Implement GET /users/{user_id}
# Filter returned fields by comma-separated ?fields= query param
# e.g. ?fields=name,email → {"name": "Alice", "email": "alice@example.com"}
# If fields not specified, return all fields (including password)

# TODO: GET /users/{user_id}/public エンドポイントを実装してください
# password を除いたパブリックフィールドのみ返す
# UserPublic response_model を使用する
# TODO: Implement GET /users/{user_id}/public
# Return only public fields (no password)
# Use UserPublic response_model
