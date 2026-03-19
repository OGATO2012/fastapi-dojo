# Problem 72: Model Config

## 概要 / Overview

Pydantic v2の `model_config` を使ったモデル設定を実装してください。
Implement model configuration using Pydantic v2 `model_config`.

## 要件 / Requirements

1. `UserStrict` モデル: `name: str`, `email: str`, `model_config = ConfigDict(str_strip_whitespace=True, str_min_length=1)` / `UserStrict` with whitespace stripping and min length
2. `UserFrozen` モデル: `name: str`, `email: str`, `model_config = ConfigDict(frozen=True)` / `UserFrozen` that is immutable
3. `POST /users/strict` - ホワイトスペースを削除して検証し、クリーンなユーザーを返す / Validates, strips whitespace, returns cleaned user
4. `POST /users/frozen` - frozenユーザーを返す / Returns frozen user

## 期待される動作 / Expected Behavior

- `UserStrict` はホワイトスペースを自動的に削除する / `UserStrict` automatically strips whitespace
- 空文字列は `str_min_length=1` のため 422 を返す / Empty string returns 422 due to `str_min_length=1`
- `UserFrozen` インスタンスは変更できない (Pythonレベルで不変) / `UserFrozen` instances are immutable at Python level
