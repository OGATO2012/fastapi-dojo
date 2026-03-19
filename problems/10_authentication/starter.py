from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

FAKE_USERS_DB = {
    "alice": {"username": "alice", "password": "secret"},
    "bob": {"username": "bob", "password": "password123"},
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# TODO: `POST /token` を実装してください。
#       - OAuth2PasswordRequestForm をフォームデータとして受け取る (Depends() を使う)
#       - ユーザー名・パスワードが一致: {"access_token": <username>, "token_type": "bearer"} を返す
#       - 不一致: 401 と {"detail": "Incorrect username or password"} を返す
#
# TODO: Implement `POST /token`.
#       - Accept OAuth2PasswordRequestForm as form data (use Depends())
#       - If credentials match: return {"access_token": <username>, "token_type": "bearer"}
#       - If not: raise 401 with detail "Incorrect username or password"


# TODO: `GET /users/me` を実装してください。
#       - oauth2_scheme で token を取得する
#       - token が FAKE_USERS_DB に存在する: {"username": <username>} を返す
#       - 存在しない: 401 と {"detail": "Invalid token"} を返す
#
# TODO: Implement `GET /users/me`.
#       - Get token via oauth2_scheme (Depends(oauth2_scheme))
#       - If token exists in FAKE_USERS_DB: return {"username": <username>}
#       - If not: raise 401 with detail "Invalid token"
