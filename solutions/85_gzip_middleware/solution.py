from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.get("/large-data")
def large_data():
    return [{"id": i, "name": f"Item {i}", "value": i * 1.5} for i in range(1, 101)]


@app.get("/small-data")
def small_data():
    return {"message": "small"}
