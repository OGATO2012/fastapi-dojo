from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UserProfile(BaseModel):
    username: str
    email: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    age: Optional[int] = None
    is_active: bool = True

@app.post("/profiles/")
def create_profile(profile: UserProfile):
    return profile

@app.get("/profiles/sample")
def get_sample_profile():
    return UserProfile(username="alice", email="alice@example.com")
