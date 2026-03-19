# Problem 36: CORS

## Topic
CORS - Add CORS middleware

## Task
Create a FastAPI application with CORS middleware configured to allow:
- Origins: "http://localhost:3000", "http://localhost:8080"
- Credentials: True
- Methods: all
- Headers: all

Implement `GET /data` that returns `{"data": "CORS-enabled response"}`.

## タスク（日本語）
CORSミドルウェアを追加したFastAPIアプリケーションを実装してください。

## Expected Behavior
- GET /data returns 200 with the expected JSON
- OPTIONS preflight from localhost:3000 returns 200 with CORS headers
- GET with Origin header includes access-control-allow-origin in response
