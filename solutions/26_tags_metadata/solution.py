from fastapi import FastAPI

app = FastAPI()


@app.get("/users/", tags=["users"], summary="List all users", description="Returns a list of all users.")
def list_users():
    return [{"id": 1, "name": "Alice"}]


@app.get("/items/", tags=["items"], summary="List all items")
def list_items():
    return [{"id": 1, "name": "Widget"}]
