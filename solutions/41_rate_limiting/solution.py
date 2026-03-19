from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI()

request_counts = {}
RATE_LIMIT = 5  # requests per minute


@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host if request.client else "unknown"
    now = time.time()
    window_start = now - 60

    if client_ip not in request_counts:
        request_counts[client_ip] = []

    # Remove old requests outside the window
    request_counts[client_ip] = [t for t in request_counts[client_ip] if t > window_start]

    if len(request_counts[client_ip]) >= RATE_LIMIT:
        return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

    request_counts[client_ip].append(now)
    return await call_next(request)


@app.get("/data")
def get_data():
    return {"data": "ok"}
