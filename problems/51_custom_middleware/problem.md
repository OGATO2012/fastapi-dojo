# Problem 51: Custom Middleware Class

## English
Implement a custom middleware using `BaseHTTPMiddleware`.

### Requirements:
- Create `CustomHeaderMiddleware(BaseHTTPMiddleware)` with `__init__` accepting `header_name` and `header_value`
- Implement `async dispatch(request, call_next)` that adds the custom header to every response
- Add middleware to the app with `header_name="X-Custom-Middleware"` and `header_value="active"`
- Create `GET /` returning `{"message": "Hello"}`

### Expected behavior:
- `GET /` → 200
- Response has header `X-Custom-Middleware: active`

---

## 日本語
`BaseHTTPMiddleware`を使ってカスタムミドルウェアを実装してください。

### 要件:
- `header_name`と`header_value`を受け取る`__init__`を持つ`CustomHeaderMiddleware(BaseHTTPMiddleware)`を作成する
- すべてのレスポンスにカスタムヘッダーを追加する`async dispatch(request, call_next)`を実装する
- `header_name="X-Custom-Middleware"`と`header_value="active"`でミドルウェアをアプリに追加する
- `{"message": "Hello"}`を返す`GET /`を作成する

### 期待される動作:
- `GET /` → 200
- レスポンスに`X-Custom-Middleware: active`ヘッダーがある
