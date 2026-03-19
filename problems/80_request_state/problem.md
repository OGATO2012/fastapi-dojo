# Problem 80: Request State

## 概要 / Overview

ミドルウェアで `request.state` にカスタムデータを設定し、エンドポイントで利用してください。
Set custom data in `request.state` via middleware and use it in endpoints.

## 要件 / Requirements

1. ミドルウェアで `request.state.request_id` にUUID文字列を設定する / Set UUID string to `request.state.request_id` in middleware
2. ミドルウェアで `request.state.start_time` に `time.time()` の値を設定する / Set `time.time()` value to `request.state.start_time` in middleware
3. `GET /info` - `{"request_id": "...", "processing_time": 0.001}` を返す / Return `{"request_id": "...", "processing_time": 0.001}`
4. `processing_time` はリクエスト開始からの経過秒数 / `processing_time` is elapsed seconds since request start

## 期待される動作 / Expected Behavior

- `GET /info` はリクエストIDと処理時間を含むJSONを返す / `GET /info` returns JSON with request ID and processing time
- request_id は有効なUUID文字列 / request_id is a valid UUID string
- processing_time は非負の数値 / processing_time is a non-negative number
