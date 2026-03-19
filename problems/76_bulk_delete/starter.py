from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items: dict[int, str] = {1: "Item 1", 2: "Item 2", 3: "Item 3", 4: "Item 4", 5: "Item 5"}


class BulkDeleteRequest(BaseModel):
    ids: list[int]


# TODO: `POST /items/bulk-delete` エンドポイントを実装してください。
# TODO: BulkDeleteRequest を受け取り、各IDを items から削除する。
# TODO: 削除できたIDを "deleted" リストに、見つからなかったIDを "not_found" リストに入れて返す。
# TODO: Implement `POST /items/bulk-delete`.
# TODO: Accept BulkDeleteRequest, delete each ID from items.
# TODO: Return {"deleted": [...], "not_found": [...]} accordingly.
