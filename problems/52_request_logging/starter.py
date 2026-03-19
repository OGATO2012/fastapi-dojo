from fastapi import FastAPI, Request
import time

app = FastAPI()

# TODO: Create module-level request_log = [] list
# TODO: モジュールレベルのrequest_log = []リストを作成する

# TODO: Add HTTP middleware log_requests(request, call_next) that:
#   - Records start_time = time.time()
#   - Calls response = await call_next(request)
#   - Calculates duration_ms = round((time.time() - start_time) * 1000, 2)
#   - Appends {"method": request.method, "path": request.url.path,
#              "status_code": response.status_code, "duration_ms": duration_ms}
#     to request_log
#   - Returns response
# TODO: HTTPミドルウェアlog_requests(request, call_next)を追加する:
#   - start_time = time.time()を記録する
#   - response = await call_next(request)を呼ぶ
#   - duration_ms = round((time.time() - start_time) * 1000, 2)を計算する
#   - {"method": request.method, "path": request.url.path,
#      "status_code": response.status_code, "duration_ms": duration_ms}
#     をrequest_logに追加する
#   - responseを返す

# TODO: Create GET /items returning {"items": ["a", "b", "c"]}
# TODO: {"items": ["a", "b", "c"]}を返すGET /itemsを作成する

# TODO: Create GET /logs returning request_log
# TODO: request_logを返すGET /logsを作成する
