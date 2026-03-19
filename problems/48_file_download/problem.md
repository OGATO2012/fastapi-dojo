# Problem 48: File Download

## English
Return a file for download from a FastAPI endpoint.

### Requirements:
- Create `GET /download/report.txt` that returns a plain text file
- Set `Content-Disposition: attachment; filename=report.txt`
- Set `Content-Type` to `text/plain`
- File content should contain meaningful text

### Expected behavior:
- `GET /download/report.txt` → 200
- `Content-Disposition` header contains `"attachment"`
- Response body is non-empty text

---

## 日本語
FastAPIエンドポイントからダウンロード用のファイルを返してください。

### 要件:
- プレーンテキストファイルを返す`GET /download/report.txt`を作成する
- `Content-Disposition: attachment; filename=report.txt`を設定する
- `Content-Type`を`text/plain`に設定する
- ファイルの内容は意味のあるテキストであること

### 期待される動作:
- `GET /download/report.txt` → 200
- `Content-Disposition`ヘッダーに`"attachment"`が含まれる
- レスポンスボディは空でないテキスト
