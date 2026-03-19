from fastapi import FastAPI, Cookie, Response
from typing import Optional

app = FastAPI()


@app.get("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="session", value="abc123")
    return {"message": "Cookie set"}


@app.get("/read-cookie")
def read_cookie(session: Optional[str] = Cookie(None)):
    return {"session": session}
