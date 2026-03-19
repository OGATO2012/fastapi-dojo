from fastapi import FastAPI, Request, Response
import hashlib
import json

app = FastAPI()

# TODO: Define DATA = {"items": ["apple", "banana", "cherry"], "version": 1}
# TODO: DATA = {"items": ["apple", "banana", "cherry"], "version": 1}を定義する

# TODO: Implement generate_etag(data: dict) -> str
#   - Serialize data to JSON with sorted keys
#   - Return MD5 hex digest of the JSON string
# TODO: generate_etag(data: dict) -> strを実装する
#   - キーをソートしてdataをJSONにシリアライズする
#   - JSON文字列のMD5ハッシュを返す

# TODO: Create GET /data endpoint that:
#   - Generates etag = f'"{generate_etag(DATA)}"'
#   - If request header "If-None-Match" equals etag, return Response(status_code=304)
#   - Otherwise set response.headers["ETag"] = etag and return DATA
# TODO: GET /dataエンドポイントを作成する:
#   - etag = f'"{generate_etag(DATA)}"'を生成する
#   - リクエストヘッダー"If-None-Match"がetagと等しい場合、Response(status_code=304)を返す
#   - それ以外はresponse.headers["ETag"] = etagを設定してDATAを返す
