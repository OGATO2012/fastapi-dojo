# Problem 32: Search

## Topic
Search - Full-text search on item names/descriptions

## Task
Create a FastAPI application with a `GET /search` endpoint that searches items by name and description.

Dataset:
- FastAPI Guide - "Learn FastAPI quickly"
- Python Tutorial - "Master Python and REST API basics"
- REST API Design - "Best practices for API design"

Query parameter: `q` (required)
Response: `{"query": q, "results": [...], "count": N}`

## タスク（日本語）
アイテムの名前と説明を全文検索できる `GET /search` エンドポイントを実装してください。

## Expected Behavior
- `?q=api` returns 3 results (all contain "api" case-insensitively)
- `?q=python` returns 1 result
- `?q=xyz` returns 0 results
