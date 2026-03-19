from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

# TODO: UserCreate モデルを作成してください (username, email, age)
# TODO: Create UserCreate model (username, email, age)

# @field_validator("username") で英数字チェックと小文字変換を実装してください
# Use @field_validator("username") for alphanumeric check and lowercase conversion

# @field_validator("email") で @ チェックと小文字変換を実装してください
# Use @field_validator("email") for @ check and lowercase conversion

# @field_validator("age") で 0〜150 の範囲チェックを実装してください
# Use @field_validator("age") for range check (0-150)

# TODO: POST /users/ エンドポイントを実装してください
# TODO: Implement POST /users/ endpoint
