# Problem 11: Custom Middleware / カスタムミドルウェア

## English

Add a custom middleware to the FastAPI app that:
1. Records the time before processing the request
2. Processes the request
3. Calculates the elapsed time
4. Adds an `X-Process-Time` header to the response with the elapsed time in seconds

## 日本語

FastAPI アプリにカスタムミドルウェアを追加してください:
1. リクエスト処理前の時刻を記録する
2. リクエストを処理する
3. 経過時間を計算する
4. レスポンスに `X-Process-Time` ヘッダーとして経過時間（秒）を追加する

## Expected Behavior

- `GET /` returns `{"message": "Hello"}`
- All responses include the `X-Process-Time` header
