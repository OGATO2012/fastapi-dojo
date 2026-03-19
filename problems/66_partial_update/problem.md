# Problem 66: Partial Update

## 概要 / Overview

PATCHエンドポイントを使って、提供されたフィールドのみを更新する部分更新を実装してください。
Implement partial updates using a PATCH endpoint that only updates provided fields.

## 要件 / Requirements

1. `UserUpdate` モデル: 全フィールドが Optional (name, email, age) / `UserUpdate` model: all fields Optional (name, email, age)
2. `User` モデル: id, name, email, age / `User` model: id, name, email, age
3. インメモリストア: `users = {1: User(id=1, name="Alice", email="alice@example.com", age=30)}` / In-memory store with initial user
4. `PATCH /users/{user_id}` - 提供されたフィールドのみ更新 / partially update user (only update provided fields)
5. `GET /users/{user_id}` - ユーザーを取得 / get user

## 期待される動作 / Expected Behavior

- PATCH with `{"name": "Bob"}` updates only the name, leaving email and age unchanged
- `.model_dump(exclude_unset=True)` を使って提供されたフィールドのみを更新する / Use `.model_dump(exclude_unset=True)` to only update provided fields
- 存在しないユーザーへのアクセスは 404 を返す / Returns 404 for non-existent users
