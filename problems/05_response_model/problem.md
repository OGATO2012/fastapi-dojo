# 問題 05: レスポンスモデル / Response Model

## 目標 / Goal

`response_model` を使ってレスポンスから特定のフィールドを除外するエンドポイントを実装してください。

Implement an endpoint that uses `response_model` to filter out specific fields from the response.

## 要件 / Requirements

### Pydanticモデル: `UserIn`

フィールド:
- `username`: `str`
- `password`: `str`
- `email`: `str`

### Pydanticモデル: `UserOut`

フィールド:
- `username`: `str`
- `email`: `str`

(`password` は含まない)

### エンドポイント: ユーザー作成

- `POST /users`
- リクエストボディとして `UserIn` を受け取る
- `response_model=UserOut` を指定して `password` を隠す
- レスポンス例 (パスワードは含まれない):
  ```json
  {"username": "alice", "email": "alice@example.com"}
  ```

## ヒント / Hints

```python
@app.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    return user
```

## テスト実行 / Run Tests

```bash
pytest problems/05_response_model/
```
