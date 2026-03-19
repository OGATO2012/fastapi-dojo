# Problem 62: Custom Error Format

## 概要 / Overview
バリデーションエラーのレスポンス形式をカスタマイズしてください。
Customize the validation error response format.

## 要件 / Requirements
1. Custom handler for `RequestValidationError` → `{"errors": [...], "message": "Validation failed"}`
2. `Item` model: `name`, `price`, `quantity`
3. `POST /items/`
