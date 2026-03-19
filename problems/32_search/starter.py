from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "FastAPI Guide", "description": "Learn FastAPI quickly"},
    {"id": 2, "name": "Python Tutorial", "description": "Master Python and REST API basics"},
    {"id": 3, "name": "REST API Design", "description": "Best practices for API design"},
]

# TODO: GETエンドポイント /search を実装してください
# - 必須クエリパラメータ: q (検索文字列)
# - name または description に q が含まれる（大文字小文字を無視）アイテムを返す
# - レスポンス形式: {"query": q, "results": [...], "count": N}
#
# TODO: Implement GET /search endpoint
# - Required query parameter: q (search string)
# - Return items where name or description contains q (case-insensitive)
# - Response format: {"query": q, "results": [...], "count": N}
