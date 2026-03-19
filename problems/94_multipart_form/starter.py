from fastapi import FastAPI, Form, UploadFile, File
from typing import Optional

app = FastAPI()

# TODO: POST /upload エンドポイントを実装してください
# フォームフィールドと UploadFile を受け取る:
#   name: str = Form(...)
#   description: str = Form(default="")
#   file: UploadFile = File(...)
# レスポンス: {"name": ..., "description": ..., "filename": file.filename, "content_type": file.content_type}
# TODO: Implement POST /upload
# Accept both form fields and UploadFile:
#   name: str = Form(...)
#   description: str = Form(default="")
#   file: UploadFile = File(...)
# Response: {"name": ..., "description": ..., "filename": file.filename, "content_type": file.content_type}
