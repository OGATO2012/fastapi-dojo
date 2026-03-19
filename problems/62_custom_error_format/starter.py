from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# TODO: RequestValidationError のカスタムハンドラを実装してください
# TODO: Implement custom handler for RequestValidationError
# Use @app.exception_handler(RequestValidationError)
# Transform errors to {"field": "...", "message": "...", "type": "..."} format
# Response: {"errors": [...], "message": "Validation failed"}

# TODO: Item モデルを作成してください (name, price, quantity)
# TODO: Create Item model (name, price, quantity)

# TODO: POST /items/ エンドポイントを実装してください
# TODO: Implement POST /items/ endpoint
