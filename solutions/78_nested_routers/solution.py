from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users_router = APIRouter()
posts_router = APIRouter()

USERS = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
POSTS: dict[int, list[dict]] = {1: [{"id": 1, "title": "Hello"}], 2: []}


class PostCreate(BaseModel):
    title: str


def _get_user_or_404(user_id: int):
    for user in USERS:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@users_router.get("/users/")
def get_users():
    return USERS


@users_router.get("/users/{user_id}")
def get_user(user_id: int):
    return _get_user_or_404(user_id)


@posts_router.get("/users/{user_id}/posts")
def get_posts(user_id: int):
    _get_user_or_404(user_id)
    return POSTS.get(user_id, [])


@posts_router.post("/users/{user_id}/posts")
def create_post(user_id: int, post: PostCreate):
    _get_user_or_404(user_id)
    new_id = sum(len(v) for v in POSTS.values()) + 1
    new_post = {"id": new_id, "title": post.title}
    POSTS[user_id].append(new_post)
    return new_post


app.include_router(users_router)
app.include_router(posts_router)
