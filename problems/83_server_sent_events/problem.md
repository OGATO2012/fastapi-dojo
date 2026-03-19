# Problem 83: Server-Sent Events

## 概要 / Overview

StreamingResponse を使ってServer-Sent Events (SSE) を実装してください。
Implement Server-Sent Events (SSE) using StreamingResponse.

## 要件 / Requirements

1. `GET /events` - 5つのイベントをストリーミングする / Stream 5 events
2. 各イベントの形式は `"data: event N\n\n"` (N は 1〜5) / Each event format: `"data: event N\n\n"` (N is 1-5)
3. `media_type="text/event-stream"` を使用する / Use `media_type="text/event-stream"`
4. 同期ジェネレータを使用する（sleep不要）/ Use synchronous generator (no sleep needed)
5. `GET /status` - `{"status": "ok"}` を返す / Return `{"status": "ok"}`

## 期待される動作 / Expected Behavior

- `GET /events` は text/event-stream のレスポンスを返す / `GET /events` returns text/event-stream response
- ストリームに "data: event 1" から "data: event 5" が含まれる / Stream contains "data: event 1" through "data: event 5"
- `GET /status` は `{"status": "ok"}` を返す / `GET /status` returns `{"status": "ok"}`
