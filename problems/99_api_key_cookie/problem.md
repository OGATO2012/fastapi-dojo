# Problem 99: API Key Authentication via Cookie

## 概要 / Overview

クッキーを使ったAPIキー認証を実装してください。
Implement API key authentication using cookies.

## 要件 / Requirements

1. `POST /auth/login?api_key=secret` - 有効なAPIキーで認証クッキーを設定 / Set auth cookie with valid API key
2. 無効なAPIキー → HTTP 401 / Invalid key → 401
3. `GET /auth/protected` - 認証クッキーを検証, 無効なら 401 / Validate auth cookie, 401 if invalid
4. `POST /auth/logout` - 認証クッキーを削除 / Delete auth cookie

## 期待される動作 / Expected Behavior

- `POST /auth/login?api_key=secret` → 200 + `auth_token` クッキー / 200 + auth cookie
- `POST /auth/login?api_key=wrong` → 401 / Wrong key → 401
- `GET /auth/protected` (no cookie) → 401 / No cookie → 401
- `GET /auth/protected` (valid cookie) → 200 + user data / Valid → 200
- `POST /auth/logout` → 200 + クッキー削除 / 200 + cookie deleted
