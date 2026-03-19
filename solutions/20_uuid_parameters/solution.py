from fastapi import FastAPI
from uuid import UUID

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: UUID):
    return {"item_id": str(item_id)}
