from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# TODO: Pydantic モデル `UserIn` を定義してください。
#       フィールド: username (str), password (str), email (str)
# TODO: Define a Pydantic model `UserIn`.
#       Fields: username (str), password (str), email (str)


# TODO: Pydantic モデル `UserOut` を定義してください。
#       フィールド: username (str), email (str)  ← password は含めない！
# TODO: Define a Pydantic model `UserOut`.
#       Fields: username (str), email (str)  ← no password!


# TODO: `POST /users` エンドポイントを実装してください。
#       response_model=UserOut を指定して password が返されないようにしてください。
# TODO: Implement `POST /users` with response_model=UserOut so that password is NOT returned.
