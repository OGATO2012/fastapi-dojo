from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users_router = APIRouter()
posts_router = APIRouter()

USERS = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
POSTS: dict[int, list[dict]] = {1: [{"id": 1, "title": "Hello"}], 2: []}


class PostCreate(BaseModel):
    title: str


# TODO: users_router に `GET /users/` を実装してください（全ユーザーを返す）。
# TODO: users_router に `GET /users/{user_id}` を実装してください（単一ユーザーを返す。存在しなければ 404）。
# TODO: posts_router に `GET /users/{user_id}/posts` を実装してください（ユーザーの投稿一覧を返す）。
# TODO: posts_router に `POST /users/{user_id}/posts` を実装してください（投稿を作成して返す）。
# TODO: 両方のルーターを app に include してください。
# TODO: Implement `GET /users/` on users_router (return all users).
# TODO: Implement `GET /users/{user_id}` on users_router (return single user or 404).
# TODO: Implement `GET /users/{user_id}/posts` on posts_router (return user's posts).
# TODO: Implement `POST /users/{user_id}/posts` on posts_router (create and return post).
# TODO: Include both routers in app.
