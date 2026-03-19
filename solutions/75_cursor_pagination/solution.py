from typing import Optional

from fastapi import FastAPI

app = FastAPI()

all_items = [{"id": i, "name": f"Item {i}"} for i in range(1, 21)]


@app.get("/items")
def get_items(cursor: Optional[int] = None, limit: int = 10):
    if cursor is None:
        filtered = all_items
    else:
        filtered = [item for item in all_items if item["id"] > cursor]
    page_plus_one = filtered[:limit + 1]
    has_more = len(page_plus_one) > limit
    page = page_plus_one[:limit]
    next_cursor = page[-1]["id"] if has_more and page else None
    return {"items": page, "next_cursor": next_cursor}
