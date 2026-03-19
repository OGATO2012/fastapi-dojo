from fastapi import FastAPI, Request, Response
import hashlib
import json

app = FastAPI()

DATA = {"items": ["apple", "banana", "cherry"], "version": 1}


def generate_etag(data: dict) -> str:
    content = json.dumps(data, sort_keys=True)
    return hashlib.md5(content.encode()).hexdigest()


@app.get("/data")
def get_data(request: Request, response: Response):
    etag = f'"{generate_etag(DATA)}"'
    if request.headers.get("If-None-Match") == etag:
        return Response(status_code=304)
    response.headers["ETag"] = etag
    return DATA
