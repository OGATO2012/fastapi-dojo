# Problem 46: Redirect Response

## English
Implement HTTP redirects using `RedirectResponse`.

### Requirements:
- Create `GET /old-path` that redirects to `/new-path` with status code 301
- Create `GET /new-path` that returns `{"message": "You reached the new path"}`

### Expected behavior:
- `GET /old-path` (no follow) → 301 with `Location` header pointing to `/new-path`
- `GET /new-path` → 200 `{"message": "You reached the new path"}`

---

## 日本語
`RedirectResponse`を使ってHTTPリダイレクトを実装してください。

### 要件:
- ステータスコード301で`/new-path`にリダイレクトする`GET /old-path`を作成する
- `{"message": "You reached the new path"}`を返す`GET /new-path`を作成する

### 期待される動作:
- `GET /old-path`（リダイレクト非追従）→ `/new-path`を指す`Location`ヘッダー付きの301
- `GET /new-path` → 200 `{"message": "You reached the new path"}`
