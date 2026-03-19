# Problem 25: Custom Response Headers / カスタムレスポンスヘッダー

## English

Add multiple custom headers using the `Response` parameter:
1. `GET /data` adds:
   - `X-Total-Count: 42`
   - `X-API-Version: 1.0`
2. Returns `{"data": []}`

## 日本語

`Response` パラメータを使って複数のカスタムヘッダーを追加してください:
1. `GET /data` で以下のヘッダーを追加する:
   - `X-Total-Count: 42`
   - `X-API-Version: 1.0`
2. `{"data": []}` を返す

## Expected Behavior

- `GET /data` returns `{"data": []}` with both custom headers
