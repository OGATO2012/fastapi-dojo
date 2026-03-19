from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/old-path")
def old_path():
    return RedirectResponse(url="/new-path", status_code=301)


@app.get("/new-path")
def new_path():
    return {"message": "You reached the new path"}
