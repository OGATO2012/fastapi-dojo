# Problem 87: Common Headers via Dependency

## 概要 / Overview

共通ヘッダーを依存関係として複数のエンドポイントで再利用してください。
Reuse common headers as a dependency across multiple endpoints.

## 要件 / Requirements

1. `common_headers` 依存関係を実装する: `x_token` (必須), `accept_language` (デフォルト `"en"`) / Implement `common_headers` dependency: `x_token` (required), `accept_language` (default `"en"`)
2. `x_token` が `"fake-super-secret-token"` でなければ HTTP 400 を返す / Return HTTP 400 if `x_token` is not `"fake-super-secret-token"`
3. `GET /items` と `GET /users` の両方で `Depends(common_headers)` を使用する / Use `Depends(common_headers)` in both `GET /items` and `GET /users`
4. レスポンスに言語情報を含める / Include language info in response

## 期待される動作 / Expected Behavior

- `X-Token` ヘッダーなし → 422 / No `X-Token` header → 422
- 誤ったトークン → 400 / Wrong token → 400
- 正しいトークン → 200 + データと言語 / Correct token → 200 + data and language
- `Accept-Language: ja` → `language: "ja"` / Custom language is reflected
