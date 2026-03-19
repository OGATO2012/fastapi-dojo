from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class ItemCreate(BaseModel):
    name: str


# TODO: `POST /items` を実装してください。
#       ステータスコード 201 を返し、{"name": <name>, "id": 1} を返してください。
# TODO: Implement `POST /items` with status code 201.
#       Return {"name": <name>, "id": 1}.


# TODO: `DELETE /items/{item_id}` を実装してください。
#       ステータスコード 204 を返し、ボディは返さないでください (None を返す)。
# TODO: Implement `DELETE /items/{item_id}` with status code 204.
#       Return no body (return None).
