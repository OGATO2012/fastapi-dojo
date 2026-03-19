from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TODO: UserProfile モデルを作成してください
# Required: username: str, email: str
# Optional: bio, avatar_url, age (None by default)
# Default: is_active: bool = True

# TODO: POST /profiles/ エンドポイントを実装してください
# TODO: GET /profiles/sample エンドポイントを実装してください (username="alice", email="alice@example.com")
