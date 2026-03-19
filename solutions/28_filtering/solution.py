from fastapi import FastAPI
from typing import Optional, List

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "Apple", "category": "fruit"},
    {"id": 2, "name": "Banana", "category": "fruit"},
    {"id": 3, "name": "Carrot", "category": "vegetable"},
    {"id": 4, "name": "Broccoli", "category": "vegetable"},
]


@app.get("/items/")
def get_items(category: Optional[str] = None):
    if category:
        return [item for item in ITEMS if item["category"] == category]
    return ITEMS
