# 問題 06: HTTPステータスコード / HTTP Status Codes

## 目標 / Goal

適切なHTTPステータスコードを返すエンドポイントを実装してください。

Implement endpoints that return appropriate HTTP status codes.

## 要件 / Requirements

### エンドポイント 1: アイテム作成

- `POST /items`
- リクエストボディ: `{"name": str}`
- ステータスコード **201 Created** を返す
- レスポンス: `{"name": <name>, "id": 1}`

### エンドポイント 2: アイテム削除

- `DELETE /items/{item_id}`
- ステータスコード **204 No Content** を返す
- レスポンスボディなし (`None` を返す)

## ヒント / Hints

```python
from fastapi import FastAPI, status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(...):
    ...

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    return None
```

## テスト実行 / Run Tests

```bash
pytest problems/06_status_codes/
```
