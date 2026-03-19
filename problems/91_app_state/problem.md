# Problem 91: Application State with app.state

## 概要 / Overview

`app.state` を使ってアプリケーション全体で状態を共有してください。
Share state across the application using `app.state`.

## 要件 / Requirements

1. `app.state.counter = 0` で初期化 / Initialize `app.state.counter = 0`
2. ミドルウェアでリクエストごとにカウンターをインクリメント / Middleware increments counter per request
3. `GET /counter` - `{"counter": N}` を返す / Return `{"counter": N}`
4. `GET /reset` - カウンターを 0 にリセットして `{"counter": 0}` を返す / Reset to 0

## 期待される動作 / Expected Behavior

- 各リクエストでカウンターが増加する / Counter increases with each request
- `GET /reset` でカウンターが 0 になる / Counter resets to 0 on `GET /reset`
- リセット後の次のリクエストでカウンターが 1 になる / After reset, next request gives counter=1
