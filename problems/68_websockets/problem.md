# Problem 68: WebSockets

## 概要 / Overview

WebSocketエンドポイントを実装して、受信したメッセージをエコーバックしてください。
Implement a WebSocket endpoint that echoes received messages.

## 要件 / Requirements

1. `GET /` - `{"message": "WebSocket server ready"}` を返す / Returns `{"message": "WebSocket server ready"}`
2. `WS /ws` - WebSocket接続を受け入れ、テキストを受信して "Echo: " + メッセージを返す / Accept WebSocket connection, receive text, return "Echo: " + message

## 期待される動作 / Expected Behavior

- WebSocket接続後、メッセージを送信すると "Echo: " プレフィックス付きで返される / After connecting, sent messages are returned with "Echo: " prefix
- 複数のメッセージを送受信できる / Multiple messages can be sent and received
