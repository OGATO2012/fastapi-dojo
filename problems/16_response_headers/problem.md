# Problem 16: Response Headers / レスポンスヘッダー

## English

Add custom headers to a response:
1. `GET /items` adds `X-Custom-Header: my-value` to the response headers
2. Returns `{"items": []}`

## 日本語

レスポンスにカスタムヘッダーを追加してください:
1. `GET /items` でレスポンスヘッダーに `X-Custom-Header: my-value` を追加する
2. `{"items": []}` を返す

## Expected Behavior

- `GET /items` returns `{"items": []}` with `X-Custom-Header: my-value` header
