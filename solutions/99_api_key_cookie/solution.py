from fastapi import FastAPI, Cookie, Response, HTTPException, Query
from typing import Optional

app = FastAPI()

SECRET_API_KEY = "secret"
AUTH_COOKIE_NAME = "auth_token"
AUTH_COOKIE_VALUE = "authenticated_user_token"


@app.post("/auth/login")
async def login(response: Response, api_key: str = Query(...)):
    if api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    response.set_cookie(key=AUTH_COOKIE_NAME, value=AUTH_COOKIE_VALUE)
    return {"message": "logged in"}


@app.get("/auth/protected")
async def protected(auth_token: Optional[str] = Cookie(default=None)):
    if auth_token != AUTH_COOKIE_VALUE:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"user": "authenticated", "message": "access granted"}


@app.post("/auth/logout")
async def logout(response: Response):
    response.delete_cookie(key=AUTH_COOKIE_NAME)
    return {"message": "logged out"}
