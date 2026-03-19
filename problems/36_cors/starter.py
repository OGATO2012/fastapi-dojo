from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TODO: CORSMiddleware を追加してください
# - allow_origins=["http://localhost:3000", "http://localhost:8080"]
# - allow_credentials=True
# - allow_methods=["*"]
# - allow_headers=["*"]
#
# TODO: Add CORSMiddleware with:
# - allow_origins=["http://localhost:3000", "http://localhost:8080"]
# - allow_credentials=True
# - allow_methods=["*"]
# - allow_headers=["*"]

# TODO: GETエンドポイント /data を実装してください
# - {"data": "CORS-enabled response"} を返す
#
# TODO: Implement GET /data endpoint
# - Return {"data": "CORS-enabled response"}
