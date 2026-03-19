# Problem 44: Streaming Response

## English
Return a large text response using FastAPI's `StreamingResponse`.

### Requirements:
- Create an async generator `generate_data()` that yields 5 chunks: `"chunk 0\n"` through `"chunk 4\n"`
- Create `GET /stream` that returns a `StreamingResponse` with `media_type="text/plain"`

### Expected behavior:
- `GET /stream` → 200 with content-type `text/plain`
- Response body contains all 5 chunks

---

## 日本語
FastAPIの`StreamingResponse`を使って大きなテキストレスポンスを返してください。

### 要件:
- `"chunk 0\n"`から`"chunk 4\n"`までの5チャンクを返す非同期ジェネレーター`generate_data()`を作成する
- `media_type="text/plain"`の`StreamingResponse`を返す`GET /stream`を作成する

### 期待される動作:
- `GET /stream` → content-typeが`text/plain`の200
- レスポンスボディに全5チャンクが含まれる
