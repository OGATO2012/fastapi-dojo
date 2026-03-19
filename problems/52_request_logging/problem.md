# Problem 52: Request Logging

## English
Log request details using a middleware that records method, path, status code, and duration.

### Requirements:
- Create a module-level `request_log = []` list
- Add an HTTP middleware that records `{"method", "path", "status_code", "duration_ms"}` for each request
- Create `GET /items` returning `{"items": ["a", "b", "c"]}`
- Create `GET /logs` returning the `request_log` list

### Expected behavior:
- After calling `GET /items`, calling `GET /logs` should return a list containing an entry for `/items`
- Log entry has `method="GET"` and `path="/items"`

---

## 日本語
メソッド、パス、ステータスコード、所要時間を記録するミドルウェアを使ってリクエストの詳細をログに記録してください。

### 要件:
- モジュールレベルの`request_log = []`リストを作成する
- 各リクエストに対して`{"method", "path", "status_code", "duration_ms"}`を記録するHTTPミドルウェアを追加する
- `{"items": ["a", "b", "c"]}`を返す`GET /items`を作成する
- `request_log`リストを返す`GET /logs`を作成する

### 期待される動作:
- `GET /items`を呼び出した後、`GET /logs`を呼び出すと`/items`のエントリを含むリストが返る
- ログエントリには`method="GET"`と`path="/items"`がある
