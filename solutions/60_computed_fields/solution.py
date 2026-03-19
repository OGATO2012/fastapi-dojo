from fastapi import FastAPI
from pydantic import BaseModel, computed_field
from typing import List

app = FastAPI()

class Rectangle(BaseModel):
    width: float
    height: float

    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height

    @computed_field
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class ShoppingCart(BaseModel):
    items: List[dict]

    @computed_field
    @property
    def total_price(self) -> float:
        return sum(item["price"] for item in self.items)

    @computed_field
    @property
    def item_count(self) -> int:
        return len(self.items)

@app.post("/rectangle/")
def calculate_rectangle(rect: Rectangle):
    return rect

@app.post("/cart/")
def calculate_cart(cart: ShoppingCart):
    return cart
