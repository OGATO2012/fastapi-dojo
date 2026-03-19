# Problem 26: Tags and Metadata

## Topic
Tags and Metadata - Add tags and descriptions to endpoints

## Task
Create a FastAPI application with two endpoints that use tags and metadata:

1. `GET /users/` - Returns a list of users, tagged with "users", with summary "List all users" and description "Returns a list of all users."
2. `GET /items/` - Returns a list of items, tagged with "items", with summary "List all items"

Each user should have "id" and "name" fields. Each item should have "id" and "name" fields.

## タスク（日本語）
タグとメタデータを使用した2つのエンドポイントを持つFastAPIアプリケーションを作成してください。

## Expected Behavior
- `GET /users/` returns 200 with a list containing at least one user with "id" and "name"
- `GET /items/` returns 200 with a list containing at least one item with "id" and "name"
