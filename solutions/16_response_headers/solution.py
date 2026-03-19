from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/items")
def get_items(response: Response):
    response.headers["X-Custom-Header"] = "my-value"
    return {"items": []}
