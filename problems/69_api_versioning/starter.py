from fastapi import APIRouter, FastAPI

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")


# TODO: v1_router に `GET /users` を実装してください。
# TODO: `[{"id": 1, "name": "Alice"}]` を返す (emailなし)。
# TODO: Implement `GET /users` on v1_router.
# TODO: Return `[{"id": 1, "name": "Alice"}]` (no email).


# TODO: v2_router に `GET /users` を実装してください。
# TODO: `[{"id": 1, "name": "Alice", "email": "alice@example.com"}]` を返す。
# TODO: Implement `GET /users` on v2_router.
# TODO: Return `[{"id": 1, "name": "Alice", "email": "alice@example.com"}]`.


# TODO: ルーターをappに登録してください / Register routers with app
