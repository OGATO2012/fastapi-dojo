# Problem 95: Include Router with Prefix and Tags

## 概要 / Overview

プレフィックスとタグを使って複数のルーターをアプリに組み込んでください。
Include multiple routers with prefixes and tags in the app.

## 要件 / Requirements

1. `admin_router` を作成: `GET /stats`, `DELETE /cache` / Create `admin_router`
2. `public_router` を作成: `GET /info`, `GET /status` / Create `public_router`
3. `admin_router` を `prefix="/admin"`, `tags=["admin"]` で include / Include with prefix and tags
4. `public_router` を `prefix="/public"`, `tags=["public"]` で include / Include with prefix and tags

## 期待される動作 / Expected Behavior

- `GET /admin/stats` → 200 / Admin stats accessible
- `DELETE /admin/cache` → 200 `{"message": "cache cleared"}` / Cache cleared
- `GET /public/info` → 200 `{"info": "public info"}` / Public info
- `GET /public/status` → 200 `{"status": "ok"}` / Public status
- `GET /stats` → 404 (プレフィックスなしは無効) / Without prefix → 404
