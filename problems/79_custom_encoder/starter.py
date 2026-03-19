import uuid
from datetime import datetime
from decimal import Decimal

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: Decimal

    model_config = {"json_encoders": {Decimal: float}}


# TODO: `GET /data` エンドポイントを実装してください。
# TODO: datetime.utcnow(), Decimal("19.99"), uuid.uuid4() を含む辞書を jsonable_encoder でシリアライズして返す。
# TODO: `POST /products` エンドポイントを実装してください。
# TODO: Product モデルを受け取り、jsonable_encoder でシリアライズして JSONResponse で返す。
# TODO: Implement `GET /data`.
# TODO: Return a dict with datetime.utcnow(), Decimal("19.99"), uuid.uuid4() serialized via jsonable_encoder.
# TODO: Implement `POST /products`.
# TODO: Accept a Product, serialize with jsonable_encoder, return as JSONResponse.
