# Problem 84: Request ID Middleware

## 概要 / Overview

すべてのレスポンスに X-Request-ID ヘッダーを付与するミドルウェアを実装してください。
Implement middleware that adds an X-Request-ID header to every response.

## 要件 / Requirements

1. すべてのレスポンスに `X-Request-ID` ヘッダー（UUID4形式）を付与するミドルウェアを実装する / Implement middleware that adds `X-Request-ID` header (UUID4) to every response
2. `GET /hello` - `{"message": "hello"}` を返す / Return `{"message": "hello"}`
3. `GET /request-id` - `{"request_id": "..."}` でリクエストIDを返す / Return `{"request_id": "..."}` with the request ID
4. request_id は `request.state` 経由でエンドポイントから取得する / Get request_id from endpoint via `request.state`

## 期待される動作 / Expected Behavior

- すべてのレスポンスに `X-Request-ID` ヘッダーが付与される / Every response has `X-Request-ID` header
- `X-Request-ID` の値は有効なUUID4文字列 / `X-Request-ID` value is a valid UUID4 string
- リクエストごとに異なるIDが生成される / Different ID generated per request
- `GET /request-id` はヘッダーと同じIDを返す / `GET /request-id` returns the same ID as in the header
