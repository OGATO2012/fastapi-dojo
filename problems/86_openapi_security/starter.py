from fastapi import FastAPI, Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_401_UNAUTHORIZED

API_KEY = "my-secret-key"
API_KEY_NAME = "X-API-Key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI(
    title="Secure API",
    # TODO: openapi_tags と security スキームを設定してください
    # TODO: Configure openapi_tags and security scheme in FastAPI app
)

# TODO: get_api_key 依存関係を実装してください
# APIキーが正しくなければ HTTP 401 を返す
# TODO: Implement get_api_key dependency
# Return HTTP 401 if API key is missing or incorrect

# TODO: GET /secure エンドポイントを実装してください
# Depends(get_api_key) を使って保護する
# TODO: Implement GET /secure endpoint protected by Depends(get_api_key)
