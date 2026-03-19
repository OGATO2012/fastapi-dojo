# Problem 15: Cookies / クッキー

## English

Implement cookie handling endpoints:
1. `GET /set-cookie` sets a cookie named `session` with value `abc123` and returns `{"message": "Cookie set"}`
2. `GET /read-cookie` reads the `session` cookie and returns `{"session": "..."}`

## 日本語

クッキー操作エンドポイントを実装してください:
1. `GET /set-cookie` で `session` という名前のクッキーを `abc123` という値でセットし、`{"message": "Cookie set"}` を返す
2. `GET /read-cookie` で `session` クッキーを読み取り、`{"session": "..."}` を返す

## Expected Behavior

- `GET /set-cookie` returns `{"message": "Cookie set"}` with `Set-Cookie` header
- `GET /read-cookie` with session cookie returns `{"session": "abc123"}`
