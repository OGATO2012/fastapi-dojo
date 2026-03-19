# Problem 94: Multipart Form with File and Fields

## 概要 / Overview

ファイルとフォームフィールドを同時に受け取るマルチパートフォームを実装してください。
Implement a multipart form that accepts both files and form fields.

## 要件 / Requirements

1. `POST /upload` - `Form()` フィールドと `UploadFile` を同時に受け取る / Accept `Form()` fields and `UploadFile`
2. `name: str = Form(...)` - 必須フィールド / Required field
3. `description: str = Form(default="")` - オプションフィールド / Optional field
4. `file: UploadFile = File(...)` - 必須ファイル / Required file
5. レスポンスにファイル名とコンテントタイプを含める / Include filename and content_type in response

## 期待される動作 / Expected Behavior

- `POST /upload` with name + description + file → 200 + all values / 200 with all values
- `description` 省略時 → デフォルト空文字 / Empty string default
- `file` なし → 422 / No file → 422
- `name` なし → 422 / No name → 422
