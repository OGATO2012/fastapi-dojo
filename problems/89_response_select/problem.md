# Problem 89: Response Field Selection

## 概要 / Overview

レスポンスのフィールドを選択・除外する機能を実装してください。
Implement response field selection and exclusion.

## 要件 / Requirements

1. `GET /users/{user_id}` - クエリパラメータ `?fields=name,email` で返すフィールドを絞り込む / Filter returned fields by `?fields=` query param
2. `fields` が未指定の場合は全フィールドを返す / Return all fields if `fields` not specified
3. `GET /users/{user_id}/public` - `response_model=UserPublic` を使って `password` を除外 / Exclude `password` using `response_model=UserPublic`
4. 存在しないユーザーは 404 を返す / Return 404 for non-existent user

## 期待される動作 / Expected Behavior

- `GET /users/1` → 全フィールド (password含む) / All fields (including password)
- `GET /users/1?fields=name,email` → `{"name": "Alice", "email": "alice@example.com"}` / Filtered
- `GET /users/1/public` → password なし / No password field
- `GET /users/999` → 404 / Not found
