# 問題 08: 依存性注入 / Dependency Injection

## 目標 / Goal

`Depends` を使って共通のクエリパラメータを依存関係として注入する仕組みを実装してください。

Use `Depends` to inject common query parameters as a shared dependency.

## 要件 / Requirements

### 依存関係: `common_pagination`

```python
def common_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

### エンドポイント 1: ユーザー一覧

- `GET /users`
- `common_pagination` を `Depends` で注入する
- レスポンス例: `{"resource": "users", "skip": 0, "limit": 10}`

### エンドポイント 2: アイテム一覧

- `GET /items`
- `common_pagination` を `Depends` で注入する
- レスポンス例: `{"resource": "items", "skip": 5, "limit": 20}`

## ヒント / Hints

```python
from fastapi import FastAPI, Depends

def common_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/users")
def list_users(pagination: dict = Depends(common_pagination)):
    return {"resource": "users", **pagination}
```

## テスト実行 / Run Tests

```bash
pytest problems/08_dependency_injection/
```
