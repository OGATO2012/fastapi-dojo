from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Event(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime


@app.post("/events")
def create_event(event: Event):
    duration = (event.end_time - event.start_time).total_seconds()
    return {
        "name": event.name,
        "start_time": event.start_time,
        "end_time": event.end_time,
        "duration_seconds": duration,
    }
