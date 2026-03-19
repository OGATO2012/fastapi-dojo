# 問題 02: パスパラメータ / Path Parameters

## 目標 / Goal

パスパラメータを使用したエンドポイントを実装してください。

Implement endpoints that use path parameters.

## 要件 / Requirements

### エンドポイント 1: ユーザー取得

- `GET /users/{user_id}`
- `user_id` は整数 (int) であること
- レスポンス例: `{"user_id": 42}`

### エンドポイント 2: アイテム取得

- `GET /items/{item_name}`
- `item_name` は文字列 (str) であること
- レスポンス例: `{"item_name": "book"}`

## ヒント / Hints

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

## テスト実行 / Run Tests

```bash
pytest problems/02_path_parameters/
```
