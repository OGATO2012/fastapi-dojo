import time
import uuid

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_request_state(request: Request, call_next):
    request.state.request_id = str(uuid.uuid4())
    request.state.start_time = time.time()
    response = await call_next(request)
    return response


@app.get("/info")
async def info(request: Request):
    processing_time = time.time() - request.state.start_time
    return {"request_id": request.state.request_id, "processing_time": processing_time}
