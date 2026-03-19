from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI()

# TODO: Create a dict to store request counts per client IP
# TODO: クライアントIPごとのリクエスト数を保存するdictを作成する

# TODO: Set RATE_LIMIT = 5 requests per minute
# TODO: RATE_LIMIT = 1分あたり5リクエストに設定する

# TODO: Add an HTTP middleware that:
#   - Gets the client IP from request.client.host
#   - Tracks timestamps of requests in a sliding 60-second window
#   - Returns 429 JSONResponse with {"detail": "Rate limit exceeded"} if limit exceeded
#   - Otherwise appends current timestamp and calls call_next(request)
# TODO: HTTPミドルウェアを追加する:
#   - request.client.hostからクライアントIPを取得
#   - 60秒のスライディングウィンドウでリクエストのタイムスタンプを追跡
#   - 制限を超えた場合は{"detail": "Rate limit exceeded"}で429を返す
#   - それ以外は現在のタイムスタンプを追加してcall_next(request)を呼ぶ

# TODO: Create GET /data endpoint returning {"data": "ok"}
# TODO: {"data": "ok"}を返すGET /dataエンドポイントを作成する
