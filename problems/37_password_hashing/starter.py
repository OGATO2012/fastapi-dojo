from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordRequest(BaseModel):
    password: str

class VerifyRequest(BaseModel):
    password: str
    hashed_password: str

# TODO: POSTエンドポイント /hash-password を実装してください
# - PasswordRequest を受け取る
# - pwd_context.hash() でパスワードをハッシュ化する
# - {"hashed_password": hashed} を返す
#
# TODO: Implement POST /hash-password endpoint
# - Accept PasswordRequest
# - Hash the password using pwd_context.hash()
# - Return {"hashed_password": hashed}

# TODO: POSTエンドポイント /verify-password を実装してください
# - VerifyRequest を受け取る
# - pwd_context.verify() でパスワードを検証する
# - {"is_valid": True/False} を返す
#
# TODO: Implement POST /verify-password endpoint
# - Accept VerifyRequest
# - Verify the password using pwd_context.verify()
# - Return {"is_valid": True/False}
