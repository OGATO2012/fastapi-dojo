from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

FAKE_DB = {
    "users": {
        1: {"id": 1, "username": "alice", "is_admin": True},
        2: {"id": 2, "username": "bob", "is_admin": False},
    }
}

# TODO: get_db() 依存関係を実装してください - フェイクDBを返す
# TODO: Implement get_db() dependency - returns fake DB

# TODO: get_current_user(db=Depends(get_db)) 依存関係を実装してください
# ユーザーID 1 をアクティブユーザーとして返す (シミュレーション)
# TODO: Implement get_current_user(db=Depends(get_db)) dependency
# Return user with id=1 as the active user (simulation)

# TODO: get_admin_user(user=Depends(get_current_user)) 依存関係を実装してください
# is_admin が False なら HTTP 403 を返す
# TODO: Implement get_admin_user(user=Depends(get_current_user))
# Return HTTP 403 if user is_admin is False

# TODO: GET /admin/dashboard エンドポイントを実装してください
# get_admin_user 依存関係を使って保護する
# TODO: Implement GET /admin/dashboard protected by get_admin_user

# TODO: GET /user/profile エンドポイントを実装してください
# get_current_user 依存関係を使って保護する
# TODO: Implement GET /user/profile protected by get_current_user
