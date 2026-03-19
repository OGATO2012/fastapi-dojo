from fastapi import FastAPI, Form, HTTPException
from typing import Annotated

app = FastAPI()

# TODO: POST /register エンドポイントを実装してください
# フォームフィールド:
#   username: str (Form) - 3文字以上, そうでなければ 422
#   email: str (Form) - "@" を含む, そうでなければ 422
#   age: int (Form) - 18以上, そうでなければ 422
# バリデーションエラーは HTTPException(status_code=422) で返す
# 成功時: {"username": ..., "email": ..., "age": ...} を返す
# TODO: Implement POST /register
# Form fields:
#   username: str (Form) - min 3 chars, else 422
#   email: str (Form) - must contain "@", else 422
#   age: int (Form) - must be 18+, else 422
# Return validation errors as HTTPException(status_code=422)
# On success: return {"username": ..., "email": ..., "age": ...}
