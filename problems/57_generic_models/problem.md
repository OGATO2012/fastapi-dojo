# Problem 57: Generic Models

## 概要 / Overview
TypeVar と Generic を使って再利用可能なページネーションレスポンスラッパーを作成してください。
Use TypeVar and Generic to create a reusable pagination response wrapper.

## 要件 / Requirements

1. ジェネリックな `PagedResponse[T]` モデルを作成してください / Create generic `PagedResponse[T]` model:
   - `items: List[T]`, `total: int`, `page: int`, `size: int`

2. モデルを定義してください / Define models:
   - `User`: `id: int`, `name: str`, `email: str`
   - `Product`: `id: int`, `name: str`, `price: float`

3. エンドポイントを実装してください / Implement endpoints:
   - `GET /users/` → `PagedResponse[User]` (query params: page=1, size=3)
   - `GET /products/` → `PagedResponse[Product]` (query params: page=1, size=3)

## 期待される動作 / Expected Behavior
- `GET /users/?page=1&size=2` → items リスト、total、page、size を返す
- `GET /products/` → 同様の構造を返す
