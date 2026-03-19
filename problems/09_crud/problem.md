# 問題 09: CRUD操作 / CRUD Operations

## 目標 / Goal

インメモリのデータストアを使って、完全なCRUD (Create / Read / Update / Delete) エンドポイントを実装してください。

Implement a complete CRUD (Create / Read / Update / Delete) API using an in-memory data store.

## 要件 / Requirements

### Pydanticモデル

```python
class Item(BaseModel):
    name: str
    description: str = ""

class ItemOut(BaseModel):
    id: int
    name: str
    description: str
```

### データストア (変更不要)

```python
items_db: dict[int, ItemOut] = {}
next_id = 1
```

### エンドポイント

| メソッド | パス | 説明 | ステータスコード |
|---|---|---|---|
| GET | `/items` | 全アイテム取得 | 200 |
| POST | `/items` | アイテム作成 | 201 |
| GET | `/items/{item_id}` | アイテム取得 | 200 / 404 |
| PUT | `/items/{item_id}` | アイテム更新 | 200 / 404 |
| DELETE | `/items/{item_id}` | アイテム削除 | 204 / 404 |

### 詳細

- `GET /items`: 全アイテムをリストで返す (`list[ItemOut]`)
- `POST /items`: 新しいアイテムを作成し、`id` を自動採番する (201)
- `GET /items/{item_id}`: 該当アイテムを返す。存在しない場合は 404
- `PUT /items/{item_id}`: 該当アイテムを更新して返す。存在しない場合は 404
- `DELETE /items/{item_id}`: 該当アイテムを削除。存在しない場合は 404。ボディなし (204)

## テスト実行 / Run Tests

```bash
pytest problems/09_crud/
```
