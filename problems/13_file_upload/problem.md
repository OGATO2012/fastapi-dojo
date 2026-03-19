# Problem 13: File Upload / ファイルアップロード

## English

Implement a file upload endpoint using `UploadFile`:
1. `POST /upload` accepts a file upload
2. Returns `{"filename": "...", "size": ...}` with the filename and file size in bytes

## 日本語

`UploadFile` を使ってファイルアップロードエンドポイントを実装してください:
1. `POST /upload` でファイルをアップロードできる
2. ファイル名とファイルサイズ（バイト数）を `{"filename": "...", "size": ...}` 形式で返す

## Expected Behavior

- `POST /upload` with a file returns `{"filename": "example.txt", "size": 13}`
