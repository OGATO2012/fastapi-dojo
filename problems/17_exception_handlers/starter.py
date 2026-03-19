from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# TODO: UnicornException というカスタム例外クラスを作成してください
# TODO: app.exception_handler でこの例外を処理し、{"error": "Unicorn error: <name>"} を返してください
# TODO: GET /unicorns/{name} エンドポイントを実装して、name が "yolo" の場合に UnicornException を発生させてください
# TODO: Create a custom UnicornException class
# TODO: Register an exception handler that returns {"error": "Unicorn error: <name>"}
# TODO: Implement GET /unicorns/{name} that raises UnicornException when name is "yolo"
