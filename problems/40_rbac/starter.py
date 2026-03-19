from fastapi import FastAPI, HTTPException, Header, Depends
from typing import Optional

app = FastAPI()

USERS = {
    "admin-token": {"username": "admin", "role": "admin"},
    "user-token": {"username": "alice", "role": "user"},
}

# TODO: get_current_user 依存関係を実装してください
# - x_token ヘッダーを受け取る（必須）
# - USERS から対応するユーザーを取得する
# - ユーザーが存在しない場合は 401 を返す
# - ユーザーを返す
#
# TODO: Implement get_current_user dependency
# - Accept x_token header (required)
# - Look up the user from USERS dict
# - Raise 401 if user not found
# - Return the user

# TODO: admin_required 依存関係を実装してください
# - x_token ヘッダーを受け取る（必須）
# - ユーザーが存在しない場合は 401 を返す
# - ロールが "admin" でない場合は 403 を返す
# - ユーザーを返す
#
# TODO: Implement admin_required dependency
# - Accept x_token header (required)
# - Raise 401 if user not found
# - Raise 403 if role is not "admin"
# - Return the user

# TODO: GETエンドポイント /me を実装してください
# - get_current_user を依存として使用する
# - ユーザー情報を返す
#
# TODO: Implement GET /me endpoint
# - Use get_current_user as dependency
# - Return the user info

# TODO: GETエンドポイント /admin/dashboard を実装してください
# - admin_required を依存として使用する
# - {"message": "Welcome to admin dashboard", "user": user["username"]} を返す
#
# TODO: Implement GET /admin/dashboard endpoint
# - Use admin_required as dependency
# - Return {"message": "Welcome to admin dashboard", "user": user["username"]}
