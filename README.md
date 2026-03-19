# FastAPI Dojo 🥋

FastAPIを最速で身に着けるための問題集です。

**A problem set to learn FastAPI as fast as possible.**

## 問題一覧 / Problem List

| # | タイトル / Title | キーワード / Keywords |
|---|---|---|
| 01 | [Hello World](problems/01_hello_world/) | GET, JSON |
| 02 | [パスパラメータ / Path Parameters](problems/02_path_parameters/) | Path, Type hints |
| 03 | [クエリパラメータ / Query Parameters](problems/03_query_parameters/) | Query, Optional |
| 04 | [リクエストボディ / Request Body](problems/04_request_body/) | POST, Pydantic |
| 05 | [レスポンスモデル / Response Model](problems/05_response_model/) | response_model, Pydantic |
| 06 | [HTTPステータスコード / HTTP Status Codes](problems/06_status_codes/) | status_code, 201, 204 |
| 07 | [エラー処理 / Error Handling](problems/07_error_handling/) | HTTPException, 404 |
| 08 | [依存性注入 / Dependency Injection](problems/08_dependency_injection/) | Depends |
| 09 | [CRUD操作 / CRUD Operations](problems/09_crud/) | GET, POST, PUT, DELETE |
| 10 | [認証 / Authentication](problems/10_authentication/) | OAuth2, JWT |

## セットアップ / Setup

```bash
pip install -r requirements.txt
```

## テストの実行 / Running Tests

全問題のテストを実行 / Run all tests:

```bash
pytest
```

特定の問題のテストを実行 / Run tests for a specific problem:

```bash
pytest problems/01_hello_world/
```

## 取り組み方 / How to Work

1. `problems/XX_name/problem.md` を読んで問題を理解する
2. `problems/XX_name/starter.py` を編集して `TODO` を実装する
3. `pytest problems/XX_name/` を実行してテストがパスするか確認する
4. 詰まったら `solutions/XX_name/solution.py` を参照する

---

1. Read `problems/XX_name/problem.md` to understand the problem
2. Edit `problems/XX_name/starter.py` to implement the `TODO` sections
3. Run `pytest problems/XX_name/` to check if the tests pass
4. If stuck, refer to `solutions/XX_name/solution.py`