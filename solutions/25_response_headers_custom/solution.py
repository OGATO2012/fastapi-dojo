from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/data")
def get_data(response: Response):
    response.headers["X-Total-Count"] = "42"
    response.headers["X-API-Version"] = "1.0"
    return {"data": []}
