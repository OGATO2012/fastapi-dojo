# Problem 54: Multiple Response Models

## English
Define different response models for different HTTP status codes using the `responses` parameter.

### Requirements:
- Create `ItemResponse` model with fields: `id: int`, `name: str`, `price: float`
- Create `ErrorResponse` model with fields: `detail: str`, `code: str`
- Create `ITEMS = {1: {"id": 1, "name": "Apple", "price": 1.5}}`
- Create `GET /items/{item_id}` with `responses={200: {"model": ItemResponse}, 404: {"model": ErrorResponse}}`
- Return 404 `HTTPException` if item not found

### Expected behavior:
- `GET /items/1` → 200 with `{"id": 1, "name": "Apple", "price": 1.5}`
- `GET /items/999` → 404
- OpenAPI spec at `/openapi.json` documents both response schemas

---

## 日本語
`responses`パラメータを使って異なるHTTPステータスコードに異なるレスポンスモデルを定義してください。

### 要件:
- フィールド`id: int`, `name: str`, `price: float`を持つ`ItemResponse`モデルを作成する
- フィールド`detail: str`, `code: str`を持つ`ErrorResponse`モデルを作成する
- `ITEMS = {1: {"id": 1, "name": "Apple", "price": 1.5}}`を作成する
- `responses={200: {"model": ItemResponse}, 404: {"model": ErrorResponse}}`を持つ`GET /items/{item_id}`を作成する
- アイテムが見つからない場合は404 `HTTPException`を返す

### 期待される動作:
- `GET /items/1` → 200 `{"id": 1, "name": "Apple", "price": 1.5}`
- `GET /items/999` → 404
- `/openapi.json`のOpenAPI仕様に両方のレスポンススキーマが記載されている
