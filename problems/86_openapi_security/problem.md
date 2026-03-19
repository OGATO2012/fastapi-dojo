# Problem 86: OpenAPI Security Scheme

## 概要 / Overview

APIキー認証を使ってエンドポイントを保護してください。
Protect an endpoint using API key authentication.

## 要件 / Requirements

1. `APIKeyHeader` を使って `X-API-Key` ヘッダーのセキュリティスキームを定義する / Define security scheme for `X-API-Key` header using `APIKeyHeader`
2. `get_api_key` 依存関係を実装する。キーが `my-secret-key` でなければ HTTP 401 を返す / Implement `get_api_key` dependency. Return HTTP 401 if key is not `my-secret-key`
3. `GET /secure` を `Depends(get_api_key)` で保護する / Protect `GET /secure` with `Depends(get_api_key)`
4. OpenAPI スキーマにセキュリティスキームが表示される / OpenAPI schema shows security scheme

## 期待される動作 / Expected Behavior

- `GET /secure` without key → 401 / キーなし → 401
- `GET /secure` with wrong key → 401 / 誤ったキー → 401
- `GET /secure` with `X-API-Key: my-secret-key` → 200 / 正しいキー → 200
