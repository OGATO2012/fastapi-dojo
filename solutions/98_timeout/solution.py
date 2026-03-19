import time
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    return response


@app.get("/slow")
async def slow_endpoint(delay: float = 0.1):
    time.sleep(delay)
    return {"message": "slow response", "delay": delay}


@app.get("/fast")
async def fast_endpoint():
    return {"message": "fast response"}
