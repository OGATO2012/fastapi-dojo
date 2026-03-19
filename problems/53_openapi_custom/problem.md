# Problem 53: OpenAPI Customization

## English
Customize the OpenAPI documentation metadata for your FastAPI app.

### Requirements:
- Set `title="My Awesome API"`
- Set `description` containing markdown (e.g., bold text with `**`)
- Set `version="2.0.0"`
- Set `contact={"name": "API Support", "email": "support@example.com"}`
- Set `license_info={"name": "MIT"}`
- Create `GET /` returning `{"message": "Check /docs for custom OpenAPI"}`

### Expected behavior:
- `GET /openapi.json` → 200
- `info.title` equals `"My Awesome API"`
- `info.version` equals `"2.0.0"`
- `info.description` contains markdown

---

## 日本語
FastAPIアプリのOpenAPIドキュメントのメタデータをカスタマイズしてください。

### 要件:
- `title="My Awesome API"`を設定する
- マークダウンを含む`description`を設定する（例: `**`で太字）
- `version="2.0.0"`を設定する
- `contact={"name": "API Support", "email": "support@example.com"}`を設定する
- `license_info={"name": "MIT"}`を設定する
- `{"message": "Check /docs for custom OpenAPI"}`を返す`GET /`を作成する

### 期待される動作:
- `GET /openapi.json` → 200
- `info.title`が`"My Awesome API"`と等しい
- `info.version`が`"2.0.0"`と等しい
- `info.description`がマークダウンを含む
