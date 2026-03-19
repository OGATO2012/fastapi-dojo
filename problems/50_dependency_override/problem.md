# Problem 50: Dependency Override

## English
Override dependencies in FastAPI for testing purposes.

### Requirements:
- Create `get_database()` that returns `{"type": "production", "data": ["real_item_1", "real_item_2"]}`
- Create `get_items_from_db(db: dict = Depends(get_database))` that returns `db["data"]`
- Create `GET /items/` that returns `{"items": items}` using `Depends(get_items_from_db)`
- Create `GET /db-info` that returns `{"db_type": db["type"]}` using `Depends(get_database)`

### Expected behavior:
- Normal `GET /items/` → 200 with production data
- Override `get_database` → `/items/` and `/db-info` return test data
- After clearing overrides → original production data returns

---

## 日本語
テスト目的でFastAPIの依存関係をオーバーライドしてください。

### 要件:
- `{"type": "production", "data": ["real_item_1", "real_item_2"]}`を返す`get_database()`を作成する
- `db["data"]`を返す`get_items_from_db(db: dict = Depends(get_database))`を作成する
- `Depends(get_items_from_db)`を使って`{"items": items}`を返す`GET /items/`を作成する
- `Depends(get_database)`を使って`{"db_type": db["type"]}`を返す`GET /db-info`を作成する

### 期待される動作:
- 通常の`GET /items/` → 200でプロダクションデータ
- `get_database`をオーバーライド → `/items/`と`/db-info`がテストデータを返す
- オーバーライドをクリア後 → 元のプロダクションデータが返る
