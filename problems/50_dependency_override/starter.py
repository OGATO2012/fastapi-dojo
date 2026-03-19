from fastapi import FastAPI, Depends

app = FastAPI()

# TODO: Create get_database() function that returns:
#   {"type": "production", "data": ["real_item_1", "real_item_2"]}
# TODO: 以下を返すget_database()関数を作成する:
#   {"type": "production", "data": ["real_item_1", "real_item_2"]}

# TODO: Create get_items_from_db(db: dict = Depends(get_database)) that returns db["data"]
# TODO: db["data"]を返すget_items_from_db(db: dict = Depends(get_database))を作成する

# TODO: Create GET /items/ endpoint using Depends(get_items_from_db)
#   Returns {"items": items}
# TODO: Depends(get_items_from_db)を使ったGET /items/エンドポイントを作成する
#   {"items": items}を返す

# TODO: Create GET /db-info endpoint using Depends(get_database)
#   Returns {"db_type": db["type"]}
# TODO: Depends(get_database)を使ったGET /db-infoエンドポイントを作成する
#   {"db_type": db["type"]}を返す
