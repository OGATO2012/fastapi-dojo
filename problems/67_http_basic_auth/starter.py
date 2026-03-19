import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

VALID_USERNAME = "user"
VALID_PASSWORD = "secret"


# TODO: `GET /protected` エンドポイントを実装してください。
# TODO: `security` を Depends で使用して認証情報を取得する。
# TODO: `secrets.compare_digest` を使ってユーザー名とパスワードを安全に検証する。
# TODO: 認証情報が正しければ `{"username": "user"}` を返す。
# TODO: 認証情報が間違っていれば 401 を返す。
# TODO: Implement `GET /protected`.
# TODO: Use `security` via Depends to get credentials.
# TODO: Use `secrets.compare_digest` to safely verify username and password.
# TODO: Return `{"username": "user"}` if correct, else raise 401.
