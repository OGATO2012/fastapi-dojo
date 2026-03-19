from fastapi import FastAPI, Request
import time

app = FastAPI()

# TODO: カスタムミドルウェアを追加して全レスポンスに X-Process-Time ヘッダーを付けてください
# TODO: Add a custom middleware that adds X-Process-Time header to all responses


@app.get("/")
def root():
    return {"message": "Hello"}
