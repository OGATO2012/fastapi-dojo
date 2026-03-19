# Problem 39: API Key Authentication

## Topic
API Key Authentication - Authenticate with API key in header

## Task
Create a FastAPI application with API key authentication using the X-API-Key header.

- Valid API key: "my-secret-api-key"
- `GET /protected` - Returns `{"message": "Access granted", "api_key": api_key}` if valid key
- Returns 403 if the key is invalid or missing

Use `APIKeyHeader` from `fastapi.security`.

## タスク（日本語）
X-API-Keyヘッダーを使ったAPIキー認証を実装してください。

## Expected Behavior
- GET /protected with X-API-Key: my-secret-api-key returns 200
- GET /protected with wrong key returns 403
- GET /protected without key returns 403
