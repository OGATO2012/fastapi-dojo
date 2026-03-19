# Problem 92: Form Data Validation

## 概要 / Overview

フォームデータのバリデーションを実装してください。
Implement form data validation with custom checks.

## 要件 / Requirements

1. `POST /register` - `Form()` でフォームフィールドを受け取る / Accept form fields with `Form()`
2. `username`: 3文字以上, そうでなければ 422 / min 3 chars, else 422
3. `email`: `@` を含む, そうでなければ 422 / must contain `@`, else 422
4. `age`: 18歳以上 (int), そうでなければ 422 / must be 18+ (int), else 422
5. 成功時は `{"username", "email", "age"}` を返す / Return fields on success

## 期待される動作 / Expected Behavior

- 有効なデータ → 200 + `{"username": ..., "email": ..., "age": ...}` / Valid → 200
- 短いusername → 422 / Short username → 422
- 無効なemail → 422 / Invalid email → 422
- 未成年 → 422 / Underage → 422
- age=18 → 200 (境界値) / age=18 → 200 (boundary)
