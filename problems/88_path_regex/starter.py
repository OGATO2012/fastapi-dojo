from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

# TODO: GET /items/{item_id} エンドポイントを実装してください
# item_id は正規表現 ^[a-z]{3}-[0-9]{3}$ にマッチしなければ 422 を返す
# 例: "abc-123" は有効, "ABC-123" や "ab-123" は無効
# Path(..., pattern=r"^[a-z]{3}-[0-9]{3}$") を使用してください
# TODO: Implement GET /items/{item_id}
# item_id must match regex ^[a-z]{3}-[0-9]{3}$ or return 422
# e.g. "abc-123" valid, "ABC-123" or "ab-123" invalid
# Use Path(..., pattern=r"^[a-z]{3}-[0-9]{3}$")

# TODO: GET /files/{file_path:path} エンドポイントを実装してください
# キャッチオールパスパラメータを使ってファイルパスを受け取る
# {"file_path": file_path} を返す
# TODO: Implement GET /files/{file_path:path}
# Accept any file path using catch-all path parameter
# Return {"file_path": file_path}
