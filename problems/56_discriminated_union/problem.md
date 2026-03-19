# Problem 56: Discriminated Unions

## 概要 / Overview
Pydanticの判別ユニオン（Discriminated Unions）を使って、複数のモデルを一つのフィールドで区別するAPIを作成してください。
Use Pydantic discriminated unions to distinguish between multiple models with a single field.

## 要件 / Requirements

1. `CatModel` と `DogModel` を作成してください / Create `CatModel` and `DogModel`:
   - `CatModel`: `pet_type: Literal["cat"]`, `name: str`, `meows: bool`
   - `DogModel`: `pet_type: Literal["dog"]`, `name: str`, `barks: bool`

2. `pet_type` フィールドで判別するアノテーション型 `Pet` を作成してください / Create an annotated `Pet` type discriminated by `pet_type`

3. エンドポイントを実装してください / Implement the endpoint:
   - `POST /pets/` - ペットを作成 / Create a pet

## 期待される動作 / Expected Behavior
- `{"pet_type": "cat", "name": "Kitty", "meows": true}` → CatModel を返す
- `{"pet_type": "dog", "name": "Rex", "barks": true}` → DogModel を返す
- 無効な `pet_type` → 422 Unprocessable Entity
