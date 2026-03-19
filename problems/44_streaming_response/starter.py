from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

# TODO: Create an async generator generate_data() that:
#   - Loops 5 times (i = 0..4)
#   - Yields f"chunk {i}\n" each iteration
#   - Awaits asyncio.sleep(0) each iteration
# TODO: 非同期ジェネレーターgenerate_data()を作成する:
#   - 5回ループする (i = 0..4)
#   - 各イテレーションでf"chunk {i}\n"をyieldする
#   - 各イテレーションでasyncio.sleep(0)をawaitする

# TODO: Create GET /stream endpoint that returns:
#   - StreamingResponse(generate_data(), media_type="text/plain")
# TODO: 次を返すGET /streamエンドポイントを作成する:
#   - StreamingResponse(generate_data(), media_type="text/plain")
