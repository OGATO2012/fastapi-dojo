from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/async-data")
async def get_async_data():
    await asyncio.sleep(0)
    return {"data": "async result", "type": "async"}


@app.get("/async-items/{item_id}")
async def get_async_item(item_id: int):
    await asyncio.sleep(0)
    return {"item_id": item_id, "name": f"Item {item_id}"}
