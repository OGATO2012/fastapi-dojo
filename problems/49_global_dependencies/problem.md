# Problem 49: Global Dependencies

## English
Apply a dependency to all routes using `FastAPI(dependencies=[...])`.

### Requirements:
- Create `async def verify_token(x_token: str = Header(...))` that raises HTTP 400 if `x_token != "fake-super-secret-token"`
- Create `app = FastAPI(dependencies=[Depends(verify_token)])`
- Create `GET /items/` returning `[{"item": "Foo"}, {"item": "Bar"}]`
- Create `GET /users/` returning `[{"username": "Rick"}, {"username": "Morty"}]`

### Expected behavior:
- `GET /items/` without `X-Token` header → 422
- `GET /items/` with wrong `X-Token` → 400
- `GET /items/` with `X-Token: fake-super-secret-token` → 200
- Same rules apply to `GET /users/`

---

## 日本語
`FastAPI(dependencies=[...])`を使ってすべてのルートに依存関係を適用してください。

### 要件:
- `x_token != "fake-super-secret-token"`の場合にHTTP 400を発生させる`async def verify_token(x_token: str = Header(...))`を作成する
- `app = FastAPI(dependencies=[Depends(verify_token)])`を作成する
- `[{"item": "Foo"}, {"item": "Bar"}]`を返す`GET /items/`を作成する
- `[{"username": "Rick"}, {"username": "Morty"}]`を返す`GET /users/`を作成する

### 期待される動作:
- `X-Token`ヘッダーなしの`GET /items/` → 422
- 間違った`X-Token`の`GET /items/` → 400
- `X-Token: fake-super-secret-token`の`GET /items/` → 200
- `GET /users/`にも同じルールが適用される
