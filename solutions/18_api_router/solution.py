from fastapi import FastAPI, APIRouter

app = FastAPI()

items_router = APIRouter(prefix="/items")


@items_router.get("/")
def list_items():
    return {"items": ["item1", "item2", "item3"]}


@items_router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


app.include_router(items_router)
