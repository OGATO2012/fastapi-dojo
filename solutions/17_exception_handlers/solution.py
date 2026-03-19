from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"error": f"Unicorn error: {exc.name}"},
    )


@app.get("/unicorns/{name}")
def get_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"message": f"{name.capitalize()} is a unicorn!"}
