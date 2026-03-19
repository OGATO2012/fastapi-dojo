from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/items/{item_name}")
def get_item(item_name: str):
    return {"item_name": item_name}
