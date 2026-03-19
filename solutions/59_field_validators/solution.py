from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    email: str
    age: int
    
    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v.lower()
    
    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Email must contain @")
        return v.lower()
    
    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v < 0 or v > 150:
            raise ValueError("Age must be between 0 and 150")
        return v

@app.post("/users/")
def create_user(user: UserCreate):
    return user
