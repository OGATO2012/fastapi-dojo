from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


@app.get("/items")
async def read_items(tags: List[str] = Query(default=[])):
    return {"tags": tags}


@app.get("/ids")
async def read_ids(ids: List[int] = Query(default=[])):
    return {"ids": ids}
