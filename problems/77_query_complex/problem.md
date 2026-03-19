# Problem 77: Complex Query Parameters

## 概要 / Overview

複数の検証付きクエリパラメータで商品を絞り込むエンドポイントを実装してください。
Implement an endpoint to filter products using multiple validated query parameters.

## 要件 / Requirements

1. `GET /products` エンドポイントを実装する / Implement `GET /products` endpoint
2. オプションのクエリパラメータ: `min_price` (float), `max_price` (float), `in_stock` (bool), `categories` (List[str]) / Optional query params: `min_price` (float), `max_price` (float), `in_stock` (bool), `categories` (List[str])
3. `categories` は `Query` を使ってリスト型で受け取る / Use `Query` to receive `categories` as a list
4. ハードコードされた5つの商品リストからフィルタリングする / Filter from a hardcoded list of 5 products
5. 各パラメータが指定された場合のみフィルタリングを適用する / Only apply filtering when each parameter is specified

## 期待される動作 / Expected Behavior

- パラメータなしで全商品が返される / All products returned with no parameters
- `min_price`/`max_price` で価格範囲フィルタリング / Price range filtering with `min_price`/`max_price`
- `in_stock=true` で在庫ありのみ返される / Only in-stock items returned with `in_stock=true`
- `categories=tools&categories=electronics` で複数カテゴリフィルタリング / Filter by multiple categories
