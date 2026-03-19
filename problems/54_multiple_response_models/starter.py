from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Create ItemResponse(BaseModel) with fields: id: int, name: str, price: float
# TODO: フィールドid: int, name: str, price: floatを持つItemResponse(BaseModel)を作成する

# TODO: Create ErrorResponse(BaseModel) with fields: detail: str, code: str
# TODO: フィールドdetail: str, code: strを持つErrorResponse(BaseModel)を作成する

# TODO: Create ITEMS = {1: {"id": 1, "name": "Apple", "price": 1.5}}
# TODO: ITEMS = {1: {"id": 1, "name": "Apple", "price": 1.5}}を作成する

# TODO: Create GET /items/{item_id} with responses parameter:
#   responses={200: {"model": ItemResponse}, 404: {"model": ErrorResponse}}
#   - If item_id not in ITEMS, raise HTTPException(status_code=404, detail="Item not found")
#   - Otherwise return ITEMS[item_id]
# TODO: responsesパラメータを持つGET /items/{item_id}を作成する:
#   responses={200: {"model": ItemResponse}, 404: {"model": ErrorResponse}}
#   - item_idがITEMSにない場合、HTTPException(status_code=404, detail="Item not found")を発生させる
#   - それ以外はITEMS[item_id]を返す
