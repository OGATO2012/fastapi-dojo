# Problem 23: DateTime Parameters / 日時パラメータ

## English

Use `datetime` in request bodies:
1. Create `Event` model with: `name: str`, `start_time: datetime`, `end_time: datetime`
2. `POST /events` accepts an `Event` and returns it with an additional `duration_seconds` field
   - `duration_seconds = (end_time - start_time).total_seconds()`

## 日本語

リクエストボディに `datetime` を使ってください:
1. `Event` モデルを作成する（`name: str`, `start_time: datetime`, `end_time: datetime`）
2. `POST /events` で `Event` を受け取り、`duration_seconds` フィールドを追加して返す

## Expected Behavior

- `POST /events` with ISO datetime strings returns event data plus `duration_seconds`
