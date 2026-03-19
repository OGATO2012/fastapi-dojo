from fastapi import APIRouter, FastAPI

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")


@v1_router.get("/users")
def get_users_v1():
    return [{"id": 1, "name": "Alice"}]


@v2_router.get("/users")
def get_users_v2():
    return [{"id": 1, "name": "Alice", "email": "alice@example.com"}]


app.include_router(v1_router)
app.include_router(v2_router)
