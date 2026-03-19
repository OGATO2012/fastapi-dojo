from fastapi import Depends, FastAPI

app = FastAPI()


def common_pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/users")
def list_users(pagination: dict = Depends(common_pagination)):
    return {"resource": "users", **pagination}


@app.get("/items")
def list_items(pagination: dict = Depends(common_pagination)):
    return {"resource": "items", **pagination}
