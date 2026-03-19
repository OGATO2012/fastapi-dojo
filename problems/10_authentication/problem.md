# 問題 10: 認証 / Authentication

## 目標 / Goal

OAuth2 パスワードフローを使ったシンプルな認証エンドポイントを実装してください。

Implement a simple authentication endpoint using OAuth2 password flow.

## 要件 / Requirements

### ユーザーデータ (変更不要)

```python
FAKE_USERS_DB = {
    "alice": {"username": "alice", "password": "secret"},
    "bob": {"username": "bob", "password": "password123"},
}
```

### エンドポイント 1: ログイン / Token取得

- `POST /token`
- `OAuth2PasswordRequestForm` をフォームデータとして受け取る
- ユーザー名・パスワードが一致する場合: `{"access_token": <username>, "token_type": "bearer"}` を返す
- 一致しない場合: **401 Unauthorized** と `{"detail": "Incorrect username or password"}` を返す

### エンドポイント 2: 現在のユーザー取得

- `GET /users/me`
- `OAuth2PasswordBearer` を使ったトークン検証
- トークン (= ユーザー名) が `FAKE_USERS_DB` に存在する場合: `{"username": <username>}` を返す
- 存在しない場合: **401 Unauthorized** と `{"detail": "Invalid token"}` を返す

## ヒント / Hints

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = FAKE_USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": user["username"], "token_type": "bearer"}

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    user = FAKE_USERS_DB.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": user["username"]}
```

## テスト実行 / Run Tests

```bash
pytest problems/10_authentication/
```
