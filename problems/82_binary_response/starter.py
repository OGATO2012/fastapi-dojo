from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

FILES: dict[str, bytes] = {
    "hello.txt": b"Hello, World!",
    "data.bin": b"\x00\x01\x02\x03",
}

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


# TODO: `GET /image/placeholder` エンドポイントを実装してください。
# TODO: PNG_MAGIC で始まるバイト列を media_type="image/png" で返す。
# TODO: `GET /file/{filename}` エンドポイントを実装してください。
# TODO: FILES からファイル内容を返す。見つからない場合は 404 を返す。
# TODO: Implement `GET /image/placeholder`.
# TODO: Return bytes starting with PNG_MAGIC with media_type="image/png".
# TODO: Implement `GET /file/{filename}`.
# TODO: Return file content from FILES, or raise 404 if not found.
