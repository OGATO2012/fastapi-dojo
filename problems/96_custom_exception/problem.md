# Problem 96: Custom Exception with Handler

## 概要 / Overview

カスタム例外クラスと例外ハンドラーを実装してください。
Implement a custom exception class with an exception handler.

## 要件 / Requirements

1. `UnicornException` カスタム例外クラスを定義 (`name` 属性付き) / Define `UnicornException` with `name` attribute
2. `@app.exception_handler(UnicornException)` でハンドラーを登録 / Register handler with `@app.exception_handler`
3. ハンドラーはステータスコード 418 と `{"message": "Oops! unicorn {name} did something."}` を返す / Return 418 + message
4. `GET /unicorns/{name}` - `name="forbidden"` で例外を発生させる / Raise exception for `name="forbidden"`

## 期待される動作 / Expected Behavior

- `GET /unicorns/sparkle` → 200 `{"unicorn": "sparkle"}` / Normal name → 200
- `GET /unicorns/forbidden` → 418 `{"message": "Oops! unicorn forbidden did something."}` / Forbidden → 418
- `UnicornException` クラスが `name` 属性を持つ / Exception class has `name` attribute
