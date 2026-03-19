# Problem 12: Background Tasks / バックグラウンドタスク

## English

Use FastAPI's `BackgroundTasks` to:
1. Implement `POST /send-notification` that accepts `{"message": "..."}` in the request body
2. Add a background task that logs the message (appends to an in-memory list)
3. Return `{"status": "Message sent"}` immediately

## 日本語

FastAPI の `BackgroundTasks` を使って:
1. リクエストボディで `{"message": "..."}` を受け取る `POST /send-notification` を実装する
2. メッセージをログに記録するバックグラウンドタスクを追加する（メモリ内リストに追記）
3. 即座に `{"status": "Message sent"}` を返す

## Expected Behavior

- `POST /send-notification` with `{"message": "hello"}` returns `{"status": "Message sent"}`
- The message is logged asynchronously in the background
