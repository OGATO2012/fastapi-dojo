# Problem 78: Nested Routers

## 概要 / Overview

ネストされた APIRouter を使ってユーザーと投稿のエンドポイントを実装してください。
Implement user and post endpoints using nested APIRouters.

## 要件 / Requirements

1. `users` ルーター: `GET /users/` でユーザー一覧、`GET /users/{user_id}` で単一ユーザーを返す / `users` router: `GET /users/` returns list, `GET /users/{user_id}` returns single user
2. `posts` ルーター: `GET /users/{user_id}/posts` で投稿一覧、`POST /users/{user_id}/posts` で投稿作成 / `posts` router: `GET /users/{user_id}/posts` returns posts, `POST /users/{user_id}/posts` creates post
3. 両方のルーターをメインアプリに組み込む / Include both routers in the main app
4. ユーザーが存在しない場合は 404 を返す / Return 404 if user does not exist

## 期待される動作 / Expected Behavior

- `GET /users/` → `[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]`
- `GET /users/1` → `{"id": 1, "name": "Alice"}`
- `GET /users/1/posts` → ユーザーの投稿リスト / user's post list
- `POST /users/1/posts` → 新しい投稿を作成して返す / creates and returns new post
- 存在しないユーザーへのアクセスは 404 / 404 for non-existent user
