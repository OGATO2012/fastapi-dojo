from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: validation_errors_log リストを作成してください
# TODO: Create validation_errors_log list

# TODO: RequestValidationError のカスタムハンドラを実装してください
# TODO: Implement custom handler - log {"path": str, "error_count": int}
# Response: {"detail": "Validation Error", "errors": [...], "body": ...}

# TODO: Product モデルを作成してください (name: min_length=1, price: gt=0, stock: ge=0)
# TODO: Create Product model

# TODO: POST /products/ エンドポイントを実装してください
# TODO: Implement POST /products/ endpoint

# TODO: GET /error-log エンドポイントを実装してください
# TODO: Implement GET /error-log endpoint
