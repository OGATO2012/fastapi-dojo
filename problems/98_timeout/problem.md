# Problem 98: Request Timing Middleware

## 概要 / Overview

リクエスト処理時間を計測するミドルウェアを実装してください。
Implement middleware that measures request processing time.

## 要件 / Requirements

1. `X-Process-Time` ヘッダーにリクエスト処理時間 (秒) を設定するミドルウェア / Middleware sets `X-Process-Time` header
2. `GET /slow?delay=N` - N秒スリープして `{"message": "slow response", "delay": N}` を返す / Sleep N seconds
3. `GET /fast` - すぐに `{"message": "fast response"}` を返す / Respond immediately

## 期待される動作 / Expected Behavior

- すべてのレスポンスに `X-Process-Time` ヘッダーが付く / All responses have `X-Process-Time` header
- `GET /slow?delay=0.1` の `X-Process-Time` ≥ 0.1 / Process time ≥ delay
- `GET /fast` → 200 即座に返答 / Immediate response
