# 問題 07: エラー処理 / Error Handling

## 目標 / Goal

`HTTPException` を使って適切なエラーレスポンスを返すエンドポイントを実装してください。

Implement endpoints that raise `HTTPException` to return appropriate error responses.

## 要件 / Requirements

### データ (変更不要)

```python
ITEMS = {1: "apple", 2: "banana", 3: "cherry"}
```

### エンドポイント: アイテム取得

- `GET /items/{item_id}`
- `item_id` が `ITEMS` に存在する場合: `{"id": item_id, "name": <name>}` を返す
- `item_id` が存在しない場合: **404 Not Found** と `{"detail": "Item not found"}` を返す

## ヒント / Hints

```python
from fastapi import FastAPI, HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": ITEMS[item_id]}
```

## テスト実行 / Run Tests

```bash
pytest problems/07_error_handling/
```
