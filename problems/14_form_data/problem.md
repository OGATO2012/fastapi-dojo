# Problem 14: Form Data / フォームデータ

## English

Implement a form data endpoint:
1. `POST /submit` accepts form fields: `name` (str) and `age` (int)
2. Returns `{"name": "...", "age": ...}` as JSON

## 日本語

フォームデータエンドポイントを実装してください:
1. `POST /submit` でフォームフィールド `name` (str) と `age` (int) を受け取る
2. `{"name": "...", "age": ...}` として JSON で返す

## Expected Behavior

- `POST /submit` with form data `name=Alice&age=30` returns `{"name": "Alice", "age": 30}`
