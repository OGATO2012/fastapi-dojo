from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# TODO: Pydantic モデル `Item` を定義してください。
#       フィールド: name (str), price (float), in_stock (bool, デフォルト True)
# TODO: Define a Pydantic model `Item`.
#       Fields: name (str), price (float), in_stock (bool, default True)


# TODO: `POST /items` エンドポイントを実装し、Item をリクエストボディとして受け取り、そのまま返してください。
# TODO: Implement `POST /items` that accepts an Item as request body and returns it.
