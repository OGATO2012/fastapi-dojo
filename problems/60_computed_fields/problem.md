# Problem 60: Computed Fields (Pydantic v2)

## 概要 / Overview
Pydantic v2 の `@computed_field` を使って、他のフィールドから自動計算されるフィールドを実装してください。
Use Pydantic v2's `@computed_field` to implement fields automatically calculated from other fields.

## 要件 / Requirements
1. `Rectangle` モデル: `width`, `height`, computed `area` and `perimeter`
2. `ShoppingCart` モデル: `items: List[dict]`, computed `total_price` and `item_count`
3. `POST /rectangle/` and `POST /cart/`
