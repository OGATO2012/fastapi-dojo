# Problem 45: HTML Response

## English
Return an HTML page from a FastAPI endpoint.

### Requirements:
- Create `GET /` with `response_class=HTMLResponse`
- The HTML page must contain:
  - `<title>FastAPI HTML</title>`
  - `<h1>Hello from FastAPI!</h1>`
  - A `<p>` paragraph element

### Expected behavior:
- `GET /` → 200
- `Content-Type` header contains `text/html`
- Body contains `"Hello from FastAPI!"`

---

## 日本語
FastAPIエンドポイントからHTMLページを返してください。

### 要件:
- `response_class=HTMLResponse`を設定した`GET /`を作成する
- HTMLページに以下を含める:
  - `<title>FastAPI HTML</title>`
  - `<h1>Hello from FastAPI!</h1>`
  - `<p>`段落要素

### 期待される動作:
- `GET /` → 200
- `Content-Type`ヘッダーに`text/html`が含まれる
- ボディに`"Hello from FastAPI!"`が含まれる
