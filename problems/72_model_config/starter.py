from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app = FastAPI()


# TODO: `UserStrict` モデルを実装してください。
# TODO: `str_strip_whitespace=True` と `str_min_length=1` を設定する。
# TODO: Implement `UserStrict` model.
# TODO: Configure with `str_strip_whitespace=True` and `str_min_length=1`.
class UserStrict(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, str_min_length=1)
    name: str
    email: str


# TODO: `UserFrozen` モデルを実装してください。
# TODO: `frozen=True` を設定して不変にする。
# TODO: Implement `UserFrozen` model.
# TODO: Configure with `frozen=True` to make it immutable.
class UserFrozen(BaseModel):
    model_config = ConfigDict(frozen=True)
    name: str
    email: str


# TODO: `POST /users/strict` エンドポイントを実装してください。
# TODO: `UserStrict` でバリデーションし、クリーンなユーザーを返す。
# TODO: Implement `POST /users/strict`.
# TODO: Validate with `UserStrict` and return the cleaned user.


# TODO: `POST /users/frozen` エンドポイントを実装してください。
# TODO: `UserFrozen` でバリデーションし、ユーザーを返す。
# TODO: Implement `POST /users/frozen`.
# TODO: Validate with `UserFrozen` and return the user.
