# Problem 70: Multiple File Upload

## 概要 / Overview

複数ファイルアップロードエンドポイントを実装してください。
Implement a multiple file upload endpoint.

## 要件 / Requirements

1. `POST /upload/multiple` - `files: List[UploadFile]` を受け取る / Accepts `files: List[UploadFile]`
2. 各ファイルの `{"filename": ..., "size": ...}` のリストを返す / Returns list of `{"filename": ..., "size": ...}` for each file

## 期待される動作 / Expected Behavior

- 単一ファイルでも複数ファイルでもアップロードできる / Can upload single or multiple files
- ファイルなしの場合は 422 を返す / Returns 422 with no files
- `from fastapi import UploadFile, File` と `from typing import List` を使用する / Use `from fastapi import UploadFile, File` and `from typing import List`
