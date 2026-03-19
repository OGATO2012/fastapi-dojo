from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def generate_data():
    for i in range(5):
        yield f"chunk {i}\n"
        await asyncio.sleep(0)


@app.get("/stream")
def stream_data():
    return StreamingResponse(generate_data(), media_type="text/plain")
