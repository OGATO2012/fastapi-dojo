from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/cached-data")
def get_cached_data(response: Response):
    response.headers["Cache-Control"] = "public, max-age=3600"
    return {"data": "This response is cacheable"}


@app.get("/no-cache-data")
def get_no_cache_data(response: Response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
    return {"data": "This response should not be cached"}
