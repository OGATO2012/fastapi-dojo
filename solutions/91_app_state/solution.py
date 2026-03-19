from fastapi import FastAPI, Request

app = FastAPI()

app.state.counter = 0


@app.middleware("http")
async def count_requests(request: Request, call_next):
    app.state.counter += 1
    response = await call_next(request)
    return response


@app.get("/counter")
async def get_counter():
    return {"counter": app.state.counter}


@app.get("/reset")
async def reset_counter():
    app.state.counter = 0
    return {"counter": 0}
