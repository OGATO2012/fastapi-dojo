from fastapi import FastAPI
from pydantic import BaseModel, model_validator
from typing import Optional

app = FastAPI()

# TODO: DateRange モデルを作成してください
# TODO: Create DateRange model (start_date, end_date)
# @model_validator(mode="after") で start_date < end_date を検証してください
# Use @model_validator(mode="after") to validate start_date < end_date

# TODO: UserProfile モデルを作成してください
# TODO: Create UserProfile model (username, password, confirm_password)
# @model_validator(mode="after") でパスワード一致を検証してください
# Use @model_validator(mode="after") to validate passwords match

# TODO: POST /date-range エンドポイントを実装してください
# TODO: Implement POST /date-range endpoint

# TODO: POST /register エンドポイントを実装してください
# TODO: Implement POST /register endpoint
