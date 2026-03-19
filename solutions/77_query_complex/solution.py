from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

PRODUCTS = [
    {"id": 1, "name": "Widget", "price": 9.99, "in_stock": True, "category": "tools"},
    {"id": 2, "name": "Gadget", "price": 24.99, "in_stock": False, "category": "electronics"},
    {"id": 3, "name": "Doohickey", "price": 4.99, "in_stock": True, "category": "tools"},
    {"id": 4, "name": "Thingamajig", "price": 49.99, "in_stock": True, "category": "electronics"},
    {"id": 5, "name": "Whatchamacallit", "price": 14.99, "in_stock": False, "category": "clothing"},
]


@app.get("/products")
def get_products(
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[bool] = None,
    categories: Optional[list[str]] = Query(default=None),
):
    result = PRODUCTS[:]
    if min_price is not None:
        result = [p for p in result if p["price"] >= min_price]
    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]
    if in_stock is not None:
        result = [p for p in result if p["in_stock"] == in_stock]
    if categories is not None:
        result = [p for p in result if p["category"] in categories]
    return result
