from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

# TODO: バックグラウンドタスクを使って POST /send-notification に
# TODO: message を受け取り、バックグラウンドでログに記録し、即座にレスポンスを返してください
# TODO: Use BackgroundTasks to accept POST /send-notification with a message,
# TODO: log it in background, and return response immediately
