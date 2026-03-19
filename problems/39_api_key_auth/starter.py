from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

app = FastAPI()

API_KEY = "my-secret-api-key"
api_key_header = APIKeyHeader(name="X-API-Key")

# TODO: verify_api_key 依存関係関数を実装してください
# - api_key_header から API キーを取得する
# - API_KEY と一致しない場合は 403 を返す
# - 有効な場合は api_key を返す
#
# TODO: Implement verify_api_key dependency function
# - Get the API key from api_key_header
# - Raise 403 if it doesn't match API_KEY
# - Return api_key if valid

# TODO: GETエンドポイント /protected を実装してください
# - verify_api_key を Security 依存として使用する
# - {"message": "Access granted", "api_key": api_key} を返す
#
# TODO: Implement GET /protected endpoint
# - Use verify_api_key as a Security dependency
# - Return {"message": "Access granted", "api_key": api_key}
