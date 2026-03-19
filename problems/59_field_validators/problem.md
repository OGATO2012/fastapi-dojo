# Problem 59: Field Validators (Pydantic v2)

## 概要 / Overview
Pydantic v2 の `@field_validator` を使って個別フィールドのバリデーションを実装してください。
Use Pydantic v2's `@field_validator` to implement per-field validation.

## 要件 / Requirements

1. `UserCreate` モデルを作成してください / Create `UserCreate` model:
   - `username: str`, `email: str`, `age: int`
   - `username`: 英数字のみ、小文字に変換
   - `email`: @ を含む、小文字に変換
   - `age`: 0〜150 の範囲

2. エンドポイントを実装してください / Implement endpoint:
   - `POST /users/` - ユーザーを作成

## 期待される動作 / Expected Behavior
- 有効なユーザー → 200 (username は小文字に変換)
- 英数字以外の username → 422
- @ のない email → 422
- 範囲外の age → 422
