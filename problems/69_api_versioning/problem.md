# Problem 69: API Versioning

## 概要 / Overview

APIRouterのプレフィックスを使ったAPIバージョニングを実装してください。
Implement API versioning using APIRouter with prefix.

## 要件 / Requirements

1. プレフィックス `/api/v1` の v1 ルーター / v1 router with prefix `/api/v1`
2. プレフィックス `/api/v2` の v2 ルーター / v2 router with prefix `/api/v2`
3. `GET /api/v1/users` は `[{"id": 1, "name": "Alice"}]` を返す / Returns `[{"id": 1, "name": "Alice"}]`
4. `GET /api/v2/users` は `[{"id": 1, "name": "Alice", "email": "alice@example.com"}]` を返す / Returns list with email included

## 期待される動作 / Expected Behavior

- v1はidとnameのみを含む / v1 contains only id and name
- v2はid、name、emailを含む / v2 contains id, name, and email
- `APIRouter` を使ってバージョン別にルートを管理する / Use `APIRouter` to manage routes per version
