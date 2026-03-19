# Problem 33: Health Check

## Topic
Health Check - Return service health status

## Task
Create a FastAPI application with a `GET /health` endpoint that returns the service status.

Response must include:
- `status`: "healthy"
- `timestamp`: current UTC time as ISO string
- `uptime_seconds`: seconds since app started

## タスク（日本語）
サービスのヘルスステータスを返す `GET /health` エンドポイントを実装してください。

## Expected Behavior
- GET /health returns 200
- Response contains `status` = "healthy"
- Response contains `timestamp` key
- Response contains `uptime_seconds` key
