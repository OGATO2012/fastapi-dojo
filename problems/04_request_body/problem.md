# 問題 04: リクエストボディ / Request Body

## 目標 / Goal

Pydanticモデルを使ってリクエストボディを受け取るエンドポイントを実装してください。

Implement an endpoint that accepts a request body using a Pydantic model.

## 要件 / Requirements

### Pydanticモデル: `Item`

フィールド:
- `name`: `str` (必須)
- `price`: `float` (必須)
- `in_stock`: `bool` (デフォルト: `True`)

### エンドポイント: アイテム作成

- `POST /items`
- リクエストボディとして `Item` を受け取る
- レスポンス例:
  ```json
  {"name": "apple", "price": 1.5, "in_stock": true}
  ```

## ヒント / Hints

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create_item(item: Item):
    return item
```

## テスト実行 / Run Tests

```bash
pytest problems/04_request_body/
```
