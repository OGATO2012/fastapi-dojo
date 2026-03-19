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


# TODO: `GET /products` エンドポイントを実装してください。
# TODO: オプションのクエリパラメータ min_price, max_price, in_stock, categories (List[str]) を受け取る。
# TODO: categories は Query(default=None) を使用する。
# TODO: 各パラメータが指定された場合のみフィルタリングを適用し、PRODUCTS を絞り込んで返す。
# TODO: Implement `GET /products`.
# TODO: Accept optional query params: min_price, max_price, in_stock, categories (List[str]).
# TODO: Use Query(default=None) for categories.
# TODO: Apply each filter only when provided and return filtered PRODUCTS.
