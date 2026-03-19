# Problem 43: ETag

## English
Implement ETag-based conditional responses to support efficient caching.

### Requirements:
- Create a `DATA` dict: `{"items": ["apple", "banana", "cherry"], "version": 1}`
- Implement `generate_etag(data)` using MD5 hash of sorted JSON
- Create `GET /data` that:
  - Generates the ETag for `DATA`
  - If `If-None-Match` header matches the ETag, return 304 (no body)
  - Otherwise return `DATA` with `ETag` response header set

### Expected behavior:
- First `GET /data` → 200 with `ETag` header
- Second `GET /data` with `If-None-Match: <etag>` → 304

---

## 日本語
効率的なキャッシュをサポートするETagベースの条件付きレスポンスを実装してください。

### 要件:
- `DATA` dictを作成する: `{"items": ["apple", "banana", "cherry"], "version": 1}`
- ソートされたJSONのMD5ハッシュを使って`generate_etag(data)`を実装する
- `GET /data`を作成する:
  - `DATA`のETagを生成する
  - `If-None-Match`ヘッダーがETagと一致する場合、304を返す（ボディなし）
  - それ以外は`ETag`レスポンスヘッダーを設定して`DATA`を返す

### 期待される動作:
- 最初の`GET /data` → `ETag`ヘッダー付きの200
- `If-None-Match: <etag>`を付けた2回目の`GET /data` → 304
