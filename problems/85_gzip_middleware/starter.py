from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

# TODO: GZipMiddleware を minimum_size=1000 で app に追加してください。
# TODO: Add GZipMiddleware with minimum_size=1000 to app.


# TODO: `GET /large-data` エンドポイントを実装してください。
# TODO: id, name, value を持つ 100 件のアイテムリストを返す。
# TODO: Implement `GET /large-data`.
# TODO: Return a list of 100 items each with id, name, value fields.


# TODO: `GET /small-data` エンドポイントを実装してください。{"message": "small"} を返す。
# TODO: Implement `GET /small-data`. Return {"message": "small"}.
