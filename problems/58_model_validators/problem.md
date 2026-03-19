# Problem 58: Model Validators (Pydantic v2)

## 概要 / Overview
Pydantic v2 の `@model_validator` を使って、複数フィールドにまたがるバリデーションを実装してください。
Use Pydantic v2's `@model_validator` to implement cross-field validation.

## 要件 / Requirements

1. `DateRange` モデルを作成してください / Create `DateRange` model:
   - `start_date: str`, `end_date: str`
   - `@model_validator(mode="after")` で start_date < end_date を検証

2. `UserProfile` モデルを作成してください / Create `UserProfile` model:
   - `username: str`, `password: str`, `confirm_password: str`
   - `@model_validator(mode="after")` でパスワード一致を検証

3. エンドポイントを実装してください / Implement endpoints:
   - `POST /date-range` - 日付範囲を検証
   - `POST /register` - ユーザー登録を検証

## 期待される動作 / Expected Behavior
- 有効な日付範囲 → 200
- end_date が start_date より前 → 422
- パスワード一致 → 200
- パスワード不一致 → 422
