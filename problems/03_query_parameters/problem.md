# 問題 03: クエリパラメータ / Query Parameters

## 目標 / Goal

クエリパラメータを使用したエンドポイントを実装してください。

Implement an endpoint that uses query parameters.

## 要件 / Requirements

### エンドポイント: アイテム一覧

- `GET /items`
- クエリパラメータ `skip` (int, デフォルト: `0`)
- クエリパラメータ `limit` (int, デフォルト: `10`)
- クエリパラメータ `keyword` (str, 省略可能, デフォルト: `None`)
- レスポンス例:
  ```json
  {"skip": 0, "limit": 10, "keyword": null}
  ```
  ```json
  {"skip": 5, "limit": 20, "keyword": "python"}
  ```

## ヒント / Hints

```python
from typing import Optional

@app.get("/items")
def list_items(skip: int = 0, limit: int = 10, keyword: Optional[str] = None):
    return {"skip": skip, "limit": limit, "keyword": keyword}
```

## テスト実行 / Run Tests

```bash
pytest problems/03_query_parameters/
```
