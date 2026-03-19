# Problem 67: HTTP Basic Authentication

## 概要 / Overview

HTTPBasicを使ったHTTP基本認証を実装してください。
Implement HTTP Basic Authentication using HTTPBasic.

## 要件 / Requirements

1. `from fastapi.security import HTTPBasic, HTTPBasicCredentials` を使用する / Use HTTPBasic and HTTPBasicCredentials
2. `security = HTTPBasic()` を定義する / Define `security = HTTPBasic()`
3. `GET /protected` - 認証情報を検証し、正しければ `{"username": "user"}` を返す / Verify credentials, return `{"username": "user"}` if correct
4. 認証情報: username="user", password="secret" / Credentials: username="user", password="secret"
5. 認証情報が間違っている場合は 401 を返す / Return 401 if credentials are wrong

## 期待される動作 / Expected Behavior

- 正しい認証情報でアクセスすると `{"username": "user"}` が返される / Returns `{"username": "user"}` with valid credentials
- `secrets.compare_digest` を使って安全に認証情報を比較する / Use `secrets.compare_digest` to safely compare credentials
- 誤った認証情報や認証なしでは 401 が返される / Returns 401 for wrong or missing credentials
