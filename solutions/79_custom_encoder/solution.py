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


@app.get("/data")
def get_data():
    data = {
        "datetime": datetime.utcnow(),
        "price": Decimal("19.99"),
        "id": uuid.uuid4(),
    }
    return JSONResponse(content=jsonable_encoder(data))


@app.post("/products")
def create_product(product: Product):
    return JSONResponse(content=jsonable_encoder(product))
