import time
import uuid

from fastapi import FastAPI, Request

app = FastAPI()


# TODO: ミドルウェアを追加してください。
# TODO: 各リクエストで request.state.request_id に str(uuid.uuid4()) を設定する。
# TODO: 各リクエストで request.state.start_time に time.time() を設定する。
# TODO: Add middleware.
# TODO: Set request.state.request_id = str(uuid.uuid4()) for each request.
# TODO: Set request.state.start_time = time.time() for each request.


# TODO: `GET /info` エンドポイントを実装してください。
# TODO: request.state から request_id と start_time を読み取る。
# TODO: processing_time = time.time() - request.state.start_time を計算して返す。
# TODO: Implement `GET /info`.
# TODO: Read request_id and start_time from request.state.
# TODO: Return {"request_id": ..., "processing_time": time.time() - request.state.start_time}.
