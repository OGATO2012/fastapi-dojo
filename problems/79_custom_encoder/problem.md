# Problem 79: Custom JSON Encoder

## 概要 / Overview

特殊な型（datetime、Decimal、UUID）を含むデータを正しくJSONシリアライズするエンドポイントを実装してください。
Implement endpoints that correctly JSON-serialize data containing special types (datetime, Decimal, UUID).

## 要件 / Requirements

1. `GET /data` - datetime、Decimal、UUID フィールドを含むデータを返す / Returns data with datetime, Decimal, UUID fields
2. `POST /products` - Decimal の price フィールドを持つ商品を受け取り、正しくシリアライズして返す / Accept product with Decimal price and return correctly serialized
3. `jsonable_encoder` を使ってシリアライズする / Use `jsonable_encoder` for serialization
4. Pydantic モデルの `json_encoders` または `model_config` で Decimal を float に変換する / Convert Decimal to float using `json_encoders` or `model_config`

## 期待される動作 / Expected Behavior

- `GET /data` は ISO形式の日時文字列、数値、UUID文字列を返す / `GET /data` returns ISO datetime string, numeric value, UUID string
- `POST /products` は price が数値として返される / `POST /products` returns price as numeric value
- レスポンスが JSON として正しく解析できる / Response is correctly parseable as JSON
