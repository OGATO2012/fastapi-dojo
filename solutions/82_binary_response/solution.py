from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

FILES: dict[str, bytes] = {
    "hello.txt": b"Hello, World!",
    "data.bin": b"\x00\x01\x02\x03",
}

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
FAKE_PNG = PNG_MAGIC + b"\x00" * 16


@app.get("/image/placeholder")
def placeholder_image():
    return Response(content=FAKE_PNG, media_type="image/png")


@app.get("/file/{filename}")
def get_file(filename: str):
    if filename not in FILES:
        raise HTTPException(status_code=404, detail="File not found")
    return Response(content=FILES[filename], media_type="application/octet-stream")
