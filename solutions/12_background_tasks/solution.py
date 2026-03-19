from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

logs: list[str] = []


class NotificationRequest(BaseModel):
    message: str


def log_message(message: str):
    logs.append(message)


@app.post("/send-notification")
def send_notification(request: NotificationRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(log_message, request.message)
    return {"status": "Message sent"}


@app.get("/logs")
def get_logs():
    return {"logs": logs}
