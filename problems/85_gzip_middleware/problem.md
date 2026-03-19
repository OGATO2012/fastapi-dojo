# Problem 85: GZip Middleware

## 概要 / Overview

GZip圧縮ミドルウェアを追加して、大きなレスポンスを圧縮してください。
Add GZip compression middleware to compress large responses.

## 要件 / Requirements

1. `GZipMiddleware` を `minimum_size=1000` で追加する / Add `GZipMiddleware` with `minimum_size=1000`
2. `GET /large-data` - 100件のアイテム（各 id, name, value を含む）のリストを返す / Return list of 100 items (each with id, name, value)
3. `GET /small-data` - `{"message": "small"}` を返す / Return `{"message": "small"}`

## 期待される動作 / Expected Behavior

- `Accept-Encoding: gzip` ヘッダー付きのリクエストで大きなレスポンスが圧縮される / Large response is compressed with Accept-Encoding: gzip header
- 圧縮されたレスポンスに `Content-Encoding: gzip` ヘッダーが付与される / Compressed response has `Content-Encoding: gzip` header
- 小さいレスポンスは圧縮されない（1000バイト未満）/ Small response is not compressed (under 1000 bytes)
