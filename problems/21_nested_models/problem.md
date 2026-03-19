# Problem 21: Nested Pydantic Models / ネストされた Pydantic モデル

## English

Use nested Pydantic models:
1. Create `Address` model with: `street: str`, `city: str`, `zip_code: str`
2. Create `User` model with: `name: str`, `age: int`, `address: Address`
3. `POST /users` accepts a `User` and returns it as-is

## 日本語

ネストされた Pydantic モデルを使ってください:
1. `Address` モデルを作成する（`street: str`, `city: str`, `zip_code: str`）
2. `User` モデルを作成する（`name: str`, `age: int`, `address: Address`）
3. `POST /users` で `User` を受け取り、そのまま返す

## Expected Behavior

- `POST /users` with nested JSON returns the same user data
