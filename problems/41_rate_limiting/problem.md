# Problem 41: Rate Limiting

## English
Implement a simple rate limiting middleware that limits each client IP to 5 requests per minute.

### Requirements:
- Add an HTTP middleware that tracks request counts per client IP
- Use a sliding window of 60 seconds
- Return HTTP 429 with `{"detail": "Rate limit exceeded"}` when the limit is exceeded
- Create a `GET /data` endpoint that returns `{"data": "ok"}`

### Expected behavior:
- First 5 requests to `GET /data` return 200
- The 6th request returns 429 `{"detail": "Rate limit exceeded"}`

---

## 日本語
クライアントIPごとに1分間5リクエストに制限するシンプルなレート制限ミドルウェアを実装してください。

### 要件:
- クライアントIPごとにリクエスト数を追跡するHTTPミドルウェアを追加する
- 60秒のスライディングウィンドウを使用する
- 制限を超えた場合はHTTP 429と`{"detail": "Rate limit exceeded"}`を返す
- `{"data": "ok"}`を返す`GET /data`エンドポイントを作成する

### 期待される動作:
- `GET /data`への最初の5リクエストは200を返す
- 6番目のリクエストは429 `{"detail": "Rate limit exceeded"}`を返す
