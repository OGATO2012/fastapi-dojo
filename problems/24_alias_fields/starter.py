from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: Item モデルを作成してください:
# TODO:   item_id は "id" というエイリアスで受け取る (int)
# TODO:   item_name は "name" というエイリアスで受け取る (str)
# TODO: POST /items エンドポイントを実装して、{"item_id": ..., "item_name": ...} 形式で返してください
# TODO: Create Item model where item_id has alias "id" and item_name has alias "name"
# TODO: Implement POST /items that accepts {"id": ..., "name": ...} and returns {"item_id": ..., "item_name": ...}
