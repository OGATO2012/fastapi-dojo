import uuid
from fastapi import FastAPI, Depends, Request

app = FastAPI()

_config = {"app_name": "FastAPI Dojo", "version": "1.0.0", "debug": False}

# TODO: get_request_id() 依存関係を実装してください
# 毎回新しい UUID4 文字列を返す (リクエストスコープ)
# TODO: Implement get_request_id() dependency
# Return a new UUID4 string each time (request-scoped)

# TODO: get_config() 依存関係を実装してください
# 毎回同じ _config 辞書を返す (共有設定)
# TODO: Implement get_config() dependency
# Return the same _config dict each time (shared config)

# TODO: GET /info エンドポイントを実装してください
# get_request_id と get_config の両方を Depends で注入する
# {"request_id": ..., "config": ..., "same_config": True/False} を返す
# same_config: get_config を2回呼び出した場合に同じオブジェクトかどうか
# TODO: Implement GET /info
# Inject both get_request_id and get_config via Depends
# Return {"request_id": ..., "config": ..., "same_config": True/False}
# same_config: whether calling get_config twice returns same object
