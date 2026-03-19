# Problem 61: Settings Management

## 概要 / Overview
`pydantic-settings` の `BaseSettings` を使ってアプリ設定を管理してください。
Use `pydantic-settings` `BaseSettings` to manage application settings.

## 要件 / Requirements
1. `Settings`: `app_name`, `debug`, `api_version`, `max_items`, env_prefix="APP_"
2. `@lru_cache()` で `get_settings()`
3. `GET /settings`
