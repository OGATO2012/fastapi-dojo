# Problem 100: Dependency Injection Scopes

## 概要 / Overview

異なるスコープを持つ依存関係注入を実装してください。
Implement dependency injection with different scopes (simulated).

## 要件 / Requirements

1. `get_request_id()` - 毎回新しい UUID4 を返すリクエストスコープ依存関係 / Request-scoped: returns new UUID4 each call
2. `get_config()` - 共有の設定辞書を返す依存関係 / Shared: returns same config dict
3. `GET /info` - 両方を `Depends` で注入し `{"request_id", "config", "same_config"}` を返す / Inject both via `Depends`
4. FastAPI は同一リクエスト内で同じ依存関係を一度だけ呼び出す / FastAPI calls same dependency once per request

## 期待される動作 / Expected Behavior

- `GET /info` → 200 + `{"request_id": "uuid", "config": {...}, "same_config": true}` / 200 with all fields
- `request_id` はリクエストごとに異なる UUID / Different UUID per request
- `same_config` は `true` (FastAPI が依存関係を一度だけ解決する) / `same_config` is `true`
- `config` には `app_name: "FastAPI Dojo"` が含まれる / Config has `app_name`
