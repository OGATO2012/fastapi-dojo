# Problem 82: Binary Response

## 概要 / Overview

バイナリ/バイトデータを返すエンドポイントを実装してください。
Implement endpoints that return binary/bytes data.

## 要件 / Requirements

1. `GET /image/placeholder` - PNGマジックバイト `b'\x89PNG\r\n\x1a\n'` で始まるフェイクPNGバイト列を返す / Return fake PNG bytes starting with PNG magic bytes
2. `GET /file/{filename}` - インメモリ辞書からファイル内容を返す。見つからない場合は 404 / Return file content from in-memory dict; 404 if not found
3. インメモリファイル: `{"hello.txt": b"Hello, World!", "data.bin": b"\x00\x01\x02\x03"}` / In-memory files
4. `Response` を使って適切な `media_type` でバイトを返す / Use `Response` with appropriate `media_type` to return bytes

## 期待される動作 / Expected Behavior

- `GET /image/placeholder` → `image/png` のバイナリレスポンス / Binary response with `image/png`
- `GET /file/hello.txt` → `b"Hello, World!"` のバイト列 / Bytes `b"Hello, World!"`
- `GET /file/unknown.txt` → 404 / 404
