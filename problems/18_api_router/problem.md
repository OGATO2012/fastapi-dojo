# Problem 18: APIRouter / APIルーター

## English

Organize routes using `APIRouter`:
1. Create an `APIRouter` with `prefix="/items"`
2. Add `GET /items/` that returns `{"items": ["item1", "item2", "item3"]}`
3. Add `GET /items/{item_id}` that returns `{"item_id": item_id, "name": "Item {item_id}"}`
4. Include the router in the app with `include_router`

## 日本語

`APIRouter` を使ってルートを整理してください:
1. `prefix="/items"` を持つ `APIRouter` を作成する
2. `{"items": ["item1", "item2", "item3"]}` を返す `GET /items/` を追加する
3. `{"item_id": item_id, "name": "Item {item_id}"}` を返す `GET /items/{item_id}` を追加する
4. `include_router` でルーターをアプリに追加する

## Expected Behavior

- `GET /items/` returns `{"items": ["item1", "item2", "item3"]}`
- `GET /items/42` returns `{"item_id": 42, "name": "Item 42"}`
