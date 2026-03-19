from fastapi import FastAPI, Request
import time

app = FastAPI()

request_log = []


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    log_entry = {
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "duration_ms": round(duration * 1000, 2),
    }
    request_log.append(log_entry)
    return response


@app.get("/items")
def get_items():
    return {"items": ["a", "b", "c"]}


@app.get("/logs")
def get_logs():
    return request_log
