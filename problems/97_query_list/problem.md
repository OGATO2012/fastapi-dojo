# Problem 97: Query Parameters as Lists

## 概要 / Overview

クエリパラメータでリストを受け取る方法を実装してください。
Implement query parameters that accept multiple values as lists.

## 要件 / Requirements

1. `GET /items` - `tags: List[str] = Query(default=[])` で複数タグを受け取る / Accept multiple tags
2. `GET /ids` - `ids: List[int] = Query(default=[])` で複数整数IDを受け取る / Accept multiple int IDs
3. 型が合わない場合は 422 を返す / Return 422 for type mismatch

## 期待される動作 / Expected Behavior

- `GET /items?tags=foo&tags=bar` → `{"tags": ["foo", "bar"]}` / Multiple tags
- `GET /items` → `{"tags": []}` / Empty list
- `GET /ids?ids=1&ids=2&ids=3` → `{"ids": [1, 2, 3]}` / Multiple int IDs
- `GET /ids?ids=abc` → 422 / Non-integer → 422
