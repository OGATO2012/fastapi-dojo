from fastapi import FastAPI

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "FastAPI Guide", "description": "Learn FastAPI quickly"},
    {"id": 2, "name": "Python Tutorial", "description": "Master Python and REST API basics"},
    {"id": 3, "name": "REST API Design", "description": "Best practices for API design"},
]


@app.get("/search")
def search_items(q: str):
    q_lower = q.lower()
    results = [
        item for item in ITEMS
        if q_lower in item["name"].lower() or q_lower in item["description"].lower()
    ]
    return {"query": q, "results": results, "count": len(results)}
