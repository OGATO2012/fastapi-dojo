from fastapi import FastAPI
from contextlib import asynccontextmanager

fake_db = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    fake_db["initialized"] = True
    fake_db["items"] = ["apple", "banana", "cherry"]
    yield
    fake_db.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/items")
def get_items():
    return {"items": fake_db.get("items", []), "db_initialized": fake_db.get("initialized", False)}
