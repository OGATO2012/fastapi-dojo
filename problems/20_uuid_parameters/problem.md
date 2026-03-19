# Problem 20: UUID Parameters / UUID パラメータ

## English

Use `UUID` type for path parameters:
1. `GET /items/{item_id}` accepts `item_id` as a `UUID` type
2. Returns `{"item_id": str(item_id)}`
3. Invalid UUIDs should return 422

## 日本語

パスパラメータに `UUID` 型を使ってください:
1. `GET /items/{item_id}` で `item_id` を `UUID` 型として受け取る
2. `{"item_id": str(item_id)}` を返す
3. 無効な UUID は 422 を返す

## Expected Behavior

- `GET /items/a3f1e5c2-4b8d-4e7f-9c1a-2d3b5e6f7a8b` returns `{"item_id": "a3f1e5c2-4b8d-4e7f-9c1a-2d3b5e6f7a8b"}`
- `GET /items/not-a-uuid` returns 422
