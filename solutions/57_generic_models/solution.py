from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypeVar, Generic, List, Optional

app = FastAPI()

T = TypeVar("T")

class PagedResponse(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int

class User(BaseModel):
    id: int
    name: str
    email: str

class Product(BaseModel):
    id: int
    name: str
    price: float

USERS = [User(id=i, name=f"User {i}", email=f"user{i}@example.com") for i in range(1, 6)]
PRODUCTS = [Product(id=i, name=f"Product {i}", price=float(i * 10)) for i in range(1, 6)]

@app.get("/users/", response_model=PagedResponse[User])
def get_users(page: int = 1, size: int = 3):
    start = (page - 1) * size
    return PagedResponse(items=USERS[start:start+size], total=len(USERS), page=page, size=size)

@app.get("/products/", response_model=PagedResponse[Product])
def get_products(page: int = 1, size: int = 3):
    start = (page - 1) * size
    return PagedResponse(items=PRODUCTS[start:start+size], total=len(PRODUCTS), page=page, size=size)
