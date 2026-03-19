from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
import uuid

app = FastAPI()

class TodoItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    tags: List[str] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

@app.post("/todos/")
def create_todo(todo: TodoItem):
    return todo

@app.post("/todos/minimal")
def create_minimal_todo(title: str):
    return TodoItem(title=title)
