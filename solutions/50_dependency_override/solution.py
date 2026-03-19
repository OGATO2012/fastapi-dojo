from fastapi import FastAPI, Depends

app = FastAPI()


def get_database():
    return {"type": "production", "data": ["real_item_1", "real_item_2"]}


def get_items_from_db(db: dict = Depends(get_database)):
    return db["data"]


@app.get("/items/")
def read_items(items: list = Depends(get_items_from_db)):
    return {"items": items}


@app.get("/db-info")
def get_db_info(db: dict = Depends(get_database)):
    return {"db_type": db["type"]}
