# 問題 01: Hello World

## 目標 / Goal

FastAPIアプリケーションを作成し、`GET /` にアクセスすると `{"message": "Hello, World!"}` を返すエンドポイントを実装してください。

Implement a FastAPI application that returns `{"message": "Hello, World!"}` when `GET /` is accessed.

## 要件 / Requirements

- `GET /` エンドポイントを実装する
- レスポンスは `{"message": "Hello, World!"}` であること
- ステータスコードは `200` であること

## ヒント / Hints

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "..."}
```

## テスト実行 / Run Tests

```bash
pytest problems/01_hello_world/
```
