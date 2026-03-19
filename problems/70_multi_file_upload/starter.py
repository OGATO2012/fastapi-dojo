from typing import List

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


# TODO: `POST /upload/multiple` エンドポイントを実装してください。
# TODO: `files: List[UploadFile] = File(...)` パラメータを受け取る。
# TODO: 各ファイルについて `{"filename": file.filename, "size": len(content)}` を返す。
# TODO: Implement `POST /upload/multiple`.
# TODO: Accept `files: List[UploadFile] = File(...)` parameter.
# TODO: Return a list of `{"filename": file.filename, "size": len(content)}` for each file.
