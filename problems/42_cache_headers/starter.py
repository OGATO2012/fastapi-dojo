from fastapi import FastAPI, Response

app = FastAPI()

# TODO: Create GET /cached-data endpoint that:
#   - Sets Cache-Control header to "public, max-age=3600"
#   - Returns {"data": "This response is cacheable"}
# TODO: GET /cached-dataエンドポイントを作成する:
#   - Cache-Controlヘッダーを"public, max-age=3600"に設定する
#   - {"data": "This response is cacheable"}を返す

# TODO: Create GET /no-cache-data endpoint that:
#   - Sets Cache-Control header to "no-store, no-cache, must-revalidate"
#   - Returns {"data": "This response should not be cached"}
# TODO: GET /no-cache-dataエンドポイントを作成する:
#   - Cache-Controlヘッダーを"no-store, no-cache, must-revalidate"に設定する
#   - {"data": "This response should not be cached"}を返す
