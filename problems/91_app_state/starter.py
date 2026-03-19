from fastapi import FastAPI, Request

app = FastAPI()

# TODO: app.state.counter を 0 で初期化してください
# TODO: Initialize app.state.counter to 0

# TODO: リクエストごとにカウンターをインクリメントするミドルウェアを追加してください
# app.state.counter を 1 増やす
# TODO: Add middleware to increment counter on each request
# Increment app.state.counter by 1

# TODO: GET /counter エンドポイントを実装してください
# {"counter": app.state.counter} を返す
# TODO: Implement GET /counter - return {"counter": app.state.counter}

# TODO: GET /reset エンドポイントを実装してください
# app.state.counter を 0 にリセットして {"counter": 0} を返す
# TODO: Implement GET /reset - reset counter to 0 and return {"counter": 0}
