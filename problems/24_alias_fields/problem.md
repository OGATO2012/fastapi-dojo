# Problem 24: Alias Fields / エイリアスフィールド

## English

Use `Field(alias=...)` in Pydantic models:
1. Create `Item` model where:
   - `item_id` has alias `"id"` (int)
   - `item_name` has alias `"name"` (str)
2. `POST /items` accepts `{"id": ..., "name": ...}` and returns `{"item_id": ..., "item_name": ...}`

## 日本語

Pydantic モデルで `Field(alias=...)` を使ってください:
1. `Item` モデルを作成する:
   - `item_id` のエイリアスは `"id"` (int)
   - `item_name` のエイリアスは `"name"` (str)
2. `POST /items` で `{"id": ..., "name": ...}` を受け取り、`{"item_id": ..., "item_name": ...}` を返す

## Expected Behavior

- `POST /items` with `{"id": 1, "name": "test"}` returns `{"item_id": 1, "item_name": "test"}`
