# Problem 17: Custom Exception Handlers / カスタム例外ハンドラー

## English

Implement custom exception handling:
1. Create a `UnicornException` class with a `name` attribute
2. Register an exception handler that returns `{"error": "Unicorn error: <name>"}` with status 418
3. `GET /unicorns/{name}` raises `UnicornException` when `name` is `"yolo"`

## 日本語

カスタム例外処理を実装してください:
1. `name` 属性を持つ `UnicornException` クラスを作成する
2. `{"error": "Unicorn error: <name>"}` をステータス 418 で返す例外ハンドラーを登録する
3. `GET /unicorns/{name}` で `name` が `"yolo"` の場合に `UnicornException` を発生させる

## Expected Behavior

- `GET /unicorns/bob` returns `{"message": "Bob is a unicorn!"}`
- `GET /unicorns/yolo` returns `{"error": "Unicorn error: yolo"}` with status 418
