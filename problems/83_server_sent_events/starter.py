from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


# TODO: イベントジェネレータ関数を実装してください。
# TODO: "data: event 1\n\n" から "data: event 5\n\n" を yield する同期ジェネレータ。
# TODO: Implement an event generator function.
# TODO: A synchronous generator that yields "data: event 1\n\n" through "data: event 5\n\n".


# TODO: `GET /events` エンドポイントを実装してください。
# TODO: StreamingResponse でジェネレータを返す（media_type="text/event-stream"）。
# TODO: Implement `GET /events`.
# TODO: Return a StreamingResponse with the generator (media_type="text/event-stream").


# TODO: `GET /status` エンドポイントを実装してください。{"status": "ok"} を返す。
# TODO: Implement `GET /status`. Return {"status": "ok"}.
