from fastapi import Depends, FastAPI

app = FastAPI()


# TODO: 依存関数 `common_pagination` を実装してください。
#       skip: int = 0, limit: int = 10 を受け取り {"skip": skip, "limit": limit} を返す。
# TODO: Implement the dependency function `common_pagination`.
#       Accept skip: int = 0, limit: int = 10 and return {"skip": skip, "limit": limit}.


# TODO: `GET /users` を実装してください。
#       common_pagination を Depends で注入し、{"resource": "users", "skip": ..., "limit": ...} を返す。
# TODO: Implement `GET /users` using Depends(common_pagination).
#       Return {"resource": "users", "skip": ..., "limit": ...}.


# TODO: `GET /items` を実装してください。
#       common_pagination を Depends で注入し、{"resource": "items", "skip": ..., "limit": ...} を返す。
# TODO: Implement `GET /items` using Depends(common_pagination).
#       Return {"resource": "items", "skip": ..., "limit": ...}.
