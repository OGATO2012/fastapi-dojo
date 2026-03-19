import uuid

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


@app.get("/hello")
def hello():
    return {"message": "hello"}


@app.get("/request-id")
async def get_request_id(request: Request):
    return {"request_id": request.state.request_id}
