from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
import uuid

app = FastAPI()

# TODO: TodoItem モデルを作成してください
# id: auto UUID with default_factory
# title: str (required)
# tags: List[str] default empty list with default_factory
# created_at: auto timestamp with default_factory

# TODO: POST /todos/ エンドポイントを実装してください
# TODO: POST /todos/minimal エンドポイントを実装してください (title as query param)
