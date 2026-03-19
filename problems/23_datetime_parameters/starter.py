from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# TODO: Event モデルを作成してください (name: str, start_time: datetime, end_time: datetime)
# TODO: POST /events エンドポイントを実装して Event を受け取り、
# TODO: duration_seconds (end_time - start_time の秒数) を追加して返してください
# TODO: Create Event model (name: str, start_time: datetime, end_time: datetime)
# TODO: Implement POST /events that accepts an Event and returns it with duration_seconds
