# Problem 73: Response Envelope

## 概要 / Overview

レスポンスエンベロープ/ラッパーパターンを実装してください。
Implement the response envelope/wrapper pattern.

## 要件 / Requirements

1. ジェネリック `APIResponse[T]` モデル: `success: bool`, `data: T`, `message: str` / Generic `APIResponse[T]` model
2. `User` モデル: `id: int`, `name: str`, `email: str` / `User` model
3. ユーザーデータ: Alice (id=1) と Bob (id=2) / Users: Alice (id=1) and Bob (id=2)
4. `GET /users/{user_id}` - `APIResponse[User]` を返す (success=True, message="User found") / Returns wrapped user
5. `GET /users/` - `APIResponse[List[User]]` を返す (success=True, message="Users retrieved") / Returns wrapped user list
6. ユーザーが見つからない場合: success=False, message="User not found", data=None, status 404 / 404 with failure envelope

## 期待される動作 / Expected Behavior

- 全レスポンスがエンベロープでラップされる / All responses are wrapped in the envelope
- 成功時は `success=True`、失敗時は `success=False` / success=True on success, success=False on failure
