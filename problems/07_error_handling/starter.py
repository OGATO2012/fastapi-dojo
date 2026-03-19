from fastapi import FastAPI, HTTPException

app = FastAPI()

ITEMS = {1: "apple", 2: "banana", 3: "cherry"}


# TODO: `GET /items/{item_id}` を実装してください。
#       - item_id が ITEMS に存在する場合: {"id": item_id, "name": <name>} を返す
#       - 存在しない場合: 404 と {"detail": "Item not found"} を返す
#
# TODO: Implement `GET /items/{item_id}`.
#       - If item_id exists in ITEMS: return {"id": item_id, "name": <name>}
#       - If not found: raise HTTPException with status 404 and detail "Item not found"
