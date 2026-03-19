# Problem 38: JWT Tokens

## Topic
JWT Tokens - Create and verify JWT tokens

## Task
Create a FastAPI application that creates and verifies JWT tokens using python-jose:

1. `POST /create-token` - Accept `{"username": "..."}` and return `{"access_token": "...", "token_type": "bearer"}`
2. `POST /verify-token` - Accept `{"token": "..."}` and return `{"valid": True, "username": "..."}` or 401 for invalid token

Use SECRET_KEY = "test-secret-key", ALGORITHM = "HS256", expiry = 1 hour.

## タスク（日本語）
python-joseを使ってJWTトークンの作成と検証を行うエンドポイントを実装してください。

## Expected Behavior
- POST /create-token returns access_token
- POST /verify-token with valid token returns valid=True and username
- POST /verify-token with invalid token returns 401
