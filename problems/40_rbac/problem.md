# Problem 40: RBAC

## Topic
RBAC - Role-based access control using dependencies

## Task
Create a FastAPI application with role-based access control:

Users (by token in X-Token header):
- "admin-token" → {"username": "admin", "role": "admin"}
- "user-token" → {"username": "alice", "role": "user"}

Endpoints:
1. `GET /me` - Returns current user (requires valid token, 401 if invalid)
2. `GET /admin/dashboard` - Returns admin welcome (requires admin role, 403 for non-admin, 401 for no token)

## タスク（日本語）
ロールベースのアクセス制御（RBAC）をFastAPIの依存関係を使って実装してください。

## Expected Behavior
- GET /me with X-Token: admin-token returns {"username": "admin", "role": "admin"}
- GET /me with X-Token: user-token returns {"username": "alice", "role": "user"}
- GET /admin/dashboard with admin-token returns 200
- GET /admin/dashboard with user-token returns 403
- GET /admin/dashboard without token returns 422
