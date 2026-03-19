import uuid

from fastapi import FastAPI, Request

app = FastAPI()


# TODO: ミドルウェアを追加してください。
# TODO: リクエストごとに UUID4 を生成し、request.state.request_id に設定する。
# TODO: レスポンスの "X-Request-ID" ヘッダーにそのUUIDを設定する。
# TODO: Add middleware.
# TODO: Generate a UUID4 per request and set it to request.state.request_id.
# TODO: Set the UUID as "X-Request-ID" header on the response.


# TODO: `GET /hello` エンドポイントを実装してください。{"message": "hello"} を返す。
# TODO: Implement `GET /hello`. Return {"message": "hello"}.


# TODO: `GET /request-id` エンドポイントを実装してください。
# TODO: request.state.request_id を {"request_id": ...} で返す。
# TODO: Implement `GET /request-id`.
# TODO: Return {"request_id": request.state.request_id}.
