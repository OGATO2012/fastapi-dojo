from fastapi import FastAPI, Depends, HTTPException, Header

# TODO: Create async function verify_token(x_token: str = Header(...)) that:
#   - Raises HTTPException(status_code=400, detail="X-Token header invalid")
#     if x_token != "fake-super-secret-token"
# TODO: 非同期関数verify_token(x_token: str = Header(...))を作成する:
#   - x_token != "fake-super-secret-token"の場合
#     HTTPException(status_code=400, detail="X-Token header invalid")を発生させる

# TODO: Create app with global dependency:
#   app = FastAPI(dependencies=[Depends(verify_token)])
# TODO: グローバル依存関係を持つappを作成する:
#   app = FastAPI(dependencies=[Depends(verify_token)])

# TODO: Create GET /items/ returning [{"item": "Foo"}, {"item": "Bar"}]
# TODO: [{"item": "Foo"}, {"item": "Bar"}]を返すGET /items/を作成する

# TODO: Create GET /users/ returning [{"username": "Rick"}, {"username": "Morty"}]
# TODO: [{"username": "Rick"}, {"username": "Morty"}]を返すGET /users/を作成する
