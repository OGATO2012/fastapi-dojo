from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_name: str = "X-Custom", header_value: str = "middleware"):
        super().__init__(app)
        self.header_name = header_name
        self.header_value = header_value

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers[self.header_name] = self.header_value
        return response


app.add_middleware(CustomHeaderMiddleware, header_name="X-Custom-Middleware", header_value="active")


@app.get("/")
def root():
    return {"message": "Hello"}
