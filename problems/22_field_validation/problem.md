# Problem 22: Field Validation / フィールドバリデーション

## English

Use Pydantic `Field` with constraints:
1. Create `Product` model with:
   - `name: str` — minimum 3, maximum 50 characters
   - `price: float` — must be greater than 0
   - `quantity: int` — must be between 0 and 100 (inclusive)
2. `POST /products` accepts a `Product` and returns it

## 日本語

Pydantic の `Field` を使って制約を設定してください:
1. `Product` モデルを作成する:
   - `name: str` — 最小3文字、最大50文字
   - `price: float` — 0より大きい
   - `quantity: int` — 0以上100以下
2. `POST /products` で `Product` を受け取り、返す

## Expected Behavior

- Valid product returns 200
- Name with less than 3 chars returns 422
- Negative price returns 422
- Quantity over 100 returns 422
