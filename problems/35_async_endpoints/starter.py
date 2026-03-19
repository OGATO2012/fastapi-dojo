from fastapi import FastAPI
import asyncio

app = FastAPI()

# TODO: 非同期GETエンドポイント /async-data を実装してください
# - async def を使用する
# - await asyncio.sleep(0) で非同期I/Oをシミュレートする
# - {"data": "async result", "type": "async"} を返す
#
# TODO: Implement async GET /async-data endpoint
# - Use async def
# - Simulate async I/O with await asyncio.sleep(0)
# - Return {"data": "async result", "type": "async"}

# TODO: 非同期GETエンドポイント /async-items/{item_id} を実装してください
# - async def と int 型のパスパラメータ item_id を使用する
# - await asyncio.sleep(0) を呼び出す
# - {"item_id": item_id, "name": f"Item {item_id}"} を返す
#
# TODO: Implement async GET /async-items/{item_id} endpoint
# - Use async def with int path parameter item_id
# - Call await asyncio.sleep(0)
# - Return {"item_id": item_id, "name": f"Item {item_id}"}
