# Problem 47: CSV Response

## English
Return CSV data from a FastAPI endpoint.

### Requirements:
- Create `GET /export/csv` that returns CSV data
- CSV must have header row: `id,name,price`
- Include at least 3 data rows
- Set `Content-Type` to `text/csv`
- Set `Content-Disposition: attachment; filename=items.csv`

### Expected behavior:
- `GET /export/csv` → 200
- `Content-Type` is `text/csv`
- Body starts with `"id,name,price"`
- `Content-Disposition` contains `"attachment"`

---

## 日本語
FastAPIエンドポイントからCSVデータを返してください。

### 要件:
- CSVデータを返す`GET /export/csv`を作成する
- CSVはヘッダー行を持つ: `id,name,price`
- 少なくとも3行のデータを含める
- `Content-Type`を`text/csv`に設定する
- `Content-Disposition: attachment; filename=items.csv`を設定する

### 期待される動作:
- `GET /export/csv` → 200
- `Content-Type`が`text/csv`
- ボディが`"id,name,price"`で始まる
- `Content-Disposition`に`"attachment"`が含まれる
