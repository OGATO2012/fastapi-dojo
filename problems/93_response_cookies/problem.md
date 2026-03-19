# Problem 93: Response Cookies

## 概要 / Overview

レスポンスでクッキーを設定・読み取り・削除してください。
Set, read, and delete cookies in responses.

## 要件 / Requirements

1. `POST /login` - `response.set_cookie()` で `session` クッキーを設定 / Set `session` cookie
2. `GET /profile` - `Cookie()` でセッションを読み取り, 無効なら 401 / Read session cookie, 401 if invalid
3. `POST /logout` - `response.delete_cookie()` でクッキーを削除 / Delete cookie

## 期待される動作 / Expected Behavior

- `POST /login` → 200 + `session` クッキー設定 / 200 + sets `session` cookie
- `GET /profile` (no cookie) → 401 / No cookie → 401
- `GET /profile` (valid cookie) → 200 + user data / Valid cookie → 200 + user
- `POST /logout` → 200 + `{"message": "logged out"}` / 200 + logged out
