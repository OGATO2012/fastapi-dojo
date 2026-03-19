from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


# TODO: UnicornException カスタム例外クラスを定義してください
# name 属性を持つ
# TODO: Define UnicornException custom exception class with a name attribute


# TODO: UnicornException のハンドラーを登録してください (@app.exception_handler)
# ステータスコード 418, {"message": f"Oops! unicorn {exc.name} did something."} を返す
# TODO: Register exception handler for UnicornException
# Return status 418, {"message": f"Oops! unicorn {exc.name} did something."}


# TODO: GET /unicorns/{name} エンドポイントを実装してください
# name が "forbidden" の場合 UnicornException(name=name) を raise する
# その他は {"unicorn": name} を返す
# TODO: Implement GET /unicorns/{name}
# Raise UnicornException(name=name) if name == "forbidden"
# Otherwise return {"unicorn": name}
