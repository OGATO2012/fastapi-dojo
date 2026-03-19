from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# TODO: Create CustomHeaderMiddleware(BaseHTTPMiddleware) class with:
#   - __init__(self, app, header_name: str = "X-Custom", header_value: str = "middleware")
#     that calls super().__init__(app) and stores header_name and header_value
#   - async dispatch(self, request: Request, call_next) that:
#     - Calls response = await call_next(request)
#     - Sets response.headers[self.header_name] = self.header_value
#     - Returns response
# TODO: CustomHeaderMiddleware(BaseHTTPMiddleware)クラスを作成する:
#   - __init__(self, app, header_name: str = "X-Custom", header_value: str = "middleware")
#     super().__init__(app)を呼び、header_nameとheader_valueを保存する
#   - async dispatch(self, request: Request, call_next):
#     - response = await call_next(request)を呼ぶ
#     - response.headers[self.header_name] = self.header_valueを設定する
#     - responseを返す

# TODO: Add middleware with:
#   app.add_middleware(CustomHeaderMiddleware, header_name="X-Custom-Middleware", header_value="active")
# TODO: 以下でミドルウェアを追加する:
#   app.add_middleware(CustomHeaderMiddleware, header_name="X-Custom-Middleware", header_value="active")

# TODO: Create GET / endpoint returning {"message": "Hello"}
# TODO: {"message": "Hello"}を返すGET /エンドポイントを作成する
