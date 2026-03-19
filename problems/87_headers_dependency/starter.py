from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Optional

app = FastAPI()

# TODO: common_headers 依存関係を実装してください
# x_token: str = Header(...) - 必須, "fake-super-secret-token" でなければ 400
# accept_language: str = Header(default="en")
# TODO: Implement common_headers dependency
# x_token: str = Header(...) - required, raise 400 if not "fake-super-secret-token"
# accept_language: str = Header(default="en")

# TODO: GET /items エンドポイントを実装してください
# Depends(common_headers) を使い, {"items": [...], "language": accept_language} を返す
# TODO: Implement GET /items using Depends(common_headers)

# TODO: GET /users エンドポイントを実装してください
# Depends(common_headers) を使い, {"users": [...], "language": accept_language} を返す
# TODO: Implement GET /users using Depends(common_headers)
