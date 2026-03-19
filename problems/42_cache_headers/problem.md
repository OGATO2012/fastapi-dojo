# Problem 42: Cache Headers

## English
Set appropriate `Cache-Control` headers on responses to control caching behavior.

### Requirements:
- Create `GET /cached-data` that sets `Cache-Control: public, max-age=3600`
- Create `GET /no-cache-data` that sets `Cache-Control: no-store, no-cache, must-revalidate`
- Both endpoints return JSON with a `"data"` key

### Expected behavior:
- `GET /cached-data` → 200, `Cache-Control: public, max-age=3600`
- `GET /no-cache-data` → 200, `Cache-Control: no-store, no-cache, must-revalidate`

---

## 日本語
レスポンスにキャッシュ動作を制御する`Cache-Control`ヘッダーを設定してください。

### 要件:
- `Cache-Control: public, max-age=3600`を設定する`GET /cached-data`を作成する
- `Cache-Control: no-store, no-cache, must-revalidate`を設定する`GET /no-cache-data`を作成する
- 両エンドポイントは`"data"`キーを含むJSONを返す

### 期待される動作:
- `GET /cached-data` → 200, `Cache-Control: public, max-age=3600`
- `GET /no-cache-data` → 200, `Cache-Control: no-store, no-cache, must-revalidate`
