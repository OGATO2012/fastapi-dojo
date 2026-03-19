# Problem 88: Path Parameters with Regex Validation

## 概要 / Overview

正規表現バリデーション付きパスパラメータとキャッチオールパスを実装してください。
Implement path parameters with regex validation and catch-all path.

## 要件 / Requirements

1. `GET /items/{item_id}` - `item_id` は `^[a-z]{3}-[0-9]{3}$` にマッチしなければ 422 / `item_id` must match `^[a-z]{3}-[0-9]{3}$` or 422
2. `Path(..., pattern=r"^[a-z]{3}-[0-9]{3}$")` を使用する / Use `Path(..., pattern=...)`
3. `GET /files/{file_path:path}` - キャッチオールパスパラメータ / Catch-all path parameter

## 期待される動作 / Expected Behavior

- `GET /items/abc-123` → 200 `{"item_id": "abc-123"}` / valid → 200
- `GET /items/ABC-123` → 422 / uppercase → 422
- `GET /items/ab-123` → 422 / too short → 422
- `GET /files/some/nested/path.txt` → 200 `{"file_path": "some/nested/path.txt"}` / nested path → 200
