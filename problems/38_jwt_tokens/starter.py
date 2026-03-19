from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "test-secret-key"
ALGORITHM = "HS256"

class TokenRequest(BaseModel):
    username: str

class TokenVerify(BaseModel):
    token: str

# TODO: POSTエンドポイント /create-token を実装してください
# - TokenRequest を受け取る
# - ペイロード: {"sub": username, "exp": 現在時刻 + 1時間}
# - jwt.encode() でトークンを生成する
# - {"access_token": token, "token_type": "bearer"} を返す
#
# TODO: Implement POST /create-token endpoint
# - Accept TokenRequest
# - Payload: {"sub": username, "exp": now + 1 hour}
# - Generate token with jwt.encode()
# - Return {"access_token": token, "token_type": "bearer"}

# TODO: POSTエンドポイント /verify-token を実装してください
# - TokenVerify を受け取る
# - jwt.decode() でトークンを検証する
# - 有効な場合: {"valid": True, "username": payload["sub"]} を返す
# - JWTError の場合: 401 を返す
#
# TODO: Implement POST /verify-token endpoint
# - Accept TokenVerify
# - Verify token with jwt.decode()
# - If valid: return {"valid": True, "username": payload["sub"]}
# - On JWTError: raise 401
