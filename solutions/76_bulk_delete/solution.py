from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items: dict[int, str] = {1: "Item 1", 2: "Item 2", 3: "Item 3", 4: "Item 4", 5: "Item 5"}


class BulkDeleteRequest(BaseModel):
    ids: list[int]


@app.post("/items/bulk-delete")
def bulk_delete(request: BulkDeleteRequest):
    deleted = []
    not_found = []
    for item_id in request.ids:
        if item_id in items:
            del items[item_id]
            deleted.append(item_id)
        else:
            not_found.append(item_id)
    return {"deleted": deleted, "not_found": not_found}
