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
| 11 | [ミドルウェア / Middleware](problems/11_middleware/) | BaseHTTPMiddleware |
| 12 | [バックグラウンドタスク / Background Tasks](problems/12_background_tasks/) | BackgroundTasks |
| 13 | [ファイルアップロード / File Upload](problems/13_file_upload/) | UploadFile, File |
| 14 | [フォームデータ / Form Data](problems/14_form_data/) | Form |
| 15 | [クッキー / Cookies](problems/15_cookies/) | Cookie, Response |
| 16 | [レスポンスヘッダー / Response Headers](problems/16_response_headers/) | Response, headers |
| 17 | [例外ハンドラー / Exception Handlers](problems/17_exception_handlers/) | exception_handler |
| 18 | [APIルーター / API Router](problems/18_api_router/) | APIRouter, prefix |
| 19 | [Enumパラメータ / Enum Parameters](problems/19_enum_parameters/) | Enum, Path |
| 20 | [UUIDパラメータ / UUID Parameters](problems/20_uuid_parameters/) | UUID, Path |
| 21 | [ネストモデル / Nested Models](problems/21_nested_models/) | Pydantic, nested |
| 22 | [フィールドバリデーション / Field Validation](problems/22_field_validation/) | Field, validator |
| 23 | [日時パラメータ / Datetime Parameters](problems/23_datetime_parameters/) | datetime, Query |
| 24 | [エイリアスフィールド / Alias Fields](problems/24_alias_fields/) | Field, alias |
| 25 | [カスタムレスポンスヘッダー / Custom Response Headers](problems/25_response_headers_custom/) | Response, headers |
| 26 | [タグメタデータ / Tags Metadata](problems/26_tags_metadata/) | tags, openapi_tags |
| 27 | [ページネーション / Pagination](problems/27_pagination/) | skip, limit, Query |
| 28 | [フィルタリング / Filtering](problems/28_filtering/) | Query, filter |
| 29 | [ソート / Sorting](problems/29_sorting/) | Query, sort |
| 30 | [一括作成 / Bulk Create](problems/30_bulk_create/) | List, POST |
| 31 | [ネストCRUD / Nested CRUD](problems/31_nested_crud/) | nested routes |
| 32 | [検索 / Search](problems/32_search/) | Query, search |
| 33 | [ヘルスチェック / Health Check](problems/33_health_check/) | GET, status |
| 34 | [ライフスパン / Lifespan](problems/34_lifespan/) | lifespan, startup |
| 35 | [非同期エンドポイント / Async Endpoints](problems/35_async_endpoints/) | async, await |
| 36 | [CORS](problems/36_cors/) | CORSMiddleware |
| 37 | [パスワードハッシュ / Password Hashing](problems/37_password_hashing/) | bcrypt, passlib |
| 38 | [JWTトークン / JWT Tokens](problems/38_jwt_tokens/) | JWT, python-jose |
| 39 | [APIキー認証 / API Key Auth](problems/39_api_key_auth/) | APIKeyHeader |
| 40 | [ロールベースアクセス制御 / RBAC](problems/40_rbac/) | Depends, roles |
| 41 | [レート制限 / Rate Limiting](problems/41_rate_limiting/) | Middleware, rate limit |
| 42 | [キャッシュヘッダー / Cache Headers](problems/42_cache_headers/) | Cache-Control |
| 43 | [ETag](problems/43_etag/) | ETag, If-None-Match |
| 44 | [ストリーミングレスポンス / Streaming Response](problems/44_streaming_response/) | StreamingResponse |
| 45 | [HTMLレスポンス / HTML Response](problems/45_html_response/) | HTMLResponse |
| 46 | [リダイレクト / Redirect Response](problems/46_redirect_response/) | RedirectResponse |
| 47 | [CSVレスポンス / CSV Response](problems/47_csv_response/) | StreamingResponse, CSV |
| 48 | [ファイルダウンロード / File Download](problems/48_file_download/) | FileResponse |
| 49 | [グローバル依存 / Global Dependencies](problems/49_global_dependencies/) | dependencies, app |
| 50 | [依存性オーバーライド / Dependency Override](problems/50_dependency_override/) | dependency_overrides |
| 51 | [カスタムミドルウェア / Custom Middleware](problems/51_custom_middleware/) | BaseHTTPMiddleware |
| 52 | [リクエストロギング / Request Logging](problems/52_request_logging/) | logging, Middleware |
| 53 | [OpenAPIカスタマイズ / OpenAPI Custom](problems/53_openapi_custom/) | custom_openapi |
| 54 | [複数レスポンスモデル / Multiple Response Models](problems/54_multiple_response_models/) | Union, responses |
| 55 | [ユニオン型 / Union Types](problems/55_union_types/) | Union, Pydantic |
| 56 | [判別ユニオン / Discriminated Union](problems/56_discriminated_union/) | discriminator |
| 57 | [ジェネリックモデル / Generic Models](problems/57_generic_models/) | Generic, TypeVar |
| 58 | [モデルバリデーター / Model Validators](problems/58_model_validators/) | model_validator |
| 59 | [フィールドバリデーター / Field Validators](problems/59_field_validators/) | field_validator |
| 60 | [計算フィールド / Computed Fields](problems/60_computed_fields/) | computed_field |
| 61 | [設定 / Settings](problems/61_settings/) | BaseSettings, pydantic-settings |
| 62 | [カスタムエラーフォーマット / Custom Error Format](problems/62_custom_error_format/) | JSONResponse, error |
| 63 | [バリデーションエラーハンドラー / Validation Error Handler](problems/63_validation_error_handler/) | RequestValidationError |
| 64 | [オプショナルフィールド / Optional Fields](problems/64_optional_fields/) | Optional, None |
| 65 | [デフォルトファクトリー / Default Factory](problems/65_default_factory/) | Field, default_factory |
| 66 | [部分更新 / Partial Update](problems/66_partial_update/) | PATCH, Optional |
| 67 | [HTTP基本認証 / HTTP Basic Auth](problems/67_http_basic_auth/) | HTTPBasic, secrets |
| 68 | [WebSocket](problems/68_websockets/) | WebSocket, ws |
| 69 | [APIバージョニング / API Versioning](problems/69_api_versioning/) | APIRouter, prefix |
| 70 | [複数ファイルアップロード / Multiple File Upload](problems/70_multi_file_upload/) | List[UploadFile] |
| 71 | [非同期依存 / Async Dependencies](problems/71_async_dependencies/) | async, Depends |
| 72 | [モデル設定 / Model Config](problems/72_model_config/) | ConfigDict, Pydantic v2 |
| 73 | [レスポンスエンベロープ / Response Envelope](problems/73_response_envelope/) | Generic, wrapper |
| 74 | [ソフトデリート / Soft Delete](problems/74_soft_delete/) | is_deleted, flag |
| 75 | [カーソルページネーション / Cursor Pagination](problems/75_cursor_pagination/) | cursor, next_cursor |
| 76 | [一括削除 / Bulk Delete](problems/76_bulk_delete/) | POST, bulk, ids |
| 77 | [複合クエリパラメータ / Complex Query Parameters](problems/77_query_complex/) | Query, filter, List |
| 78 | [ネストルーター / Nested Routers](problems/78_nested_routers/) | APIRouter, include_router |
| 79 | [カスタムJSONエンコーダー / Custom JSON Encoder](problems/79_custom_encoder/) | jsonable_encoder |
| 80 | [リクエストステート / Request State](problems/80_request_state/) | request.state, Middleware |
| 81 | [XMLレスポンス / XML Response](problems/81_xml_response/) | Response, application/xml |
| 82 | [バイナリレスポンス / Binary Response](problems/82_binary_response/) | Response, bytes |
| 83 | [サーバー送信イベント / Server-Sent Events](problems/83_server_sent_events/) | StreamingResponse, SSE |
| 84 | [リクエストIDミドルウェア / Request ID Middleware](problems/84_request_id/) | X-Request-ID, UUID |
| 85 | [GZip圧縮 / GZip Middleware](problems/85_gzip_middleware/) | GZipMiddleware |
| 86 | [OpenAPIセキュリティ / OpenAPI Security](problems/86_openapi_security/) | APIKeyHeader, security |
| 87 | [ヘッダー依存 / Headers Dependency](problems/87_headers_dependency/) | Header, Depends |
| 88 | [パス正規表現 / Path Regex](problems/88_path_regex/) | Path, regex, path param |
| 89 | [レスポンスフィールド選択 / Response Field Selection](problems/89_response_select/) | response_model_include |
| 90 | [依存チェーン / Dependency Chain](problems/90_dependency_chain/) | Depends, nested |
| 91 | [アプリケーションステート / App State](problems/91_app_state/) | app.state, Middleware |
| 92 | [フォームバリデーション / Form Validation](problems/92_form_validation/) | Form, validation |
| 93 | [レスポンスクッキー / Response Cookies](problems/93_response_cookies/) | Response, set_cookie |
| 94 | [マルチパートフォーム / Multipart Form](problems/94_multipart_form/) | Form, UploadFile |
| 95 | [ルータープレフィックス / Router Prefix](problems/95_include_router_prefix/) | prefix, tags, APIRouter |
| 96 | [カスタム例外 / Custom Exception](problems/96_custom_exception/) | exception_handler, 418 |
| 97 | [クエリリスト / Query List Parameters](problems/97_query_list/) | Query, List, multi-value |
| 98 | [タイミングミドルウェア / Timing Middleware](problems/98_timeout/) | X-Process-Time, Middleware |
| 99 | [クッキーAPIキー / API Key Cookie](problems/99_api_key_cookie/) | Cookie, APIKeyCookie |
| 100 | [依存スコープ / Dependency Scopes](problems/100_dependency_scopes/) | Depends, singleton, scoped |

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