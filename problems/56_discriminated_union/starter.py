from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Literal, Annotated
from pydantic import Field

app = FastAPI()

# TODO: CatModel を作成してください (pet_type: Literal["cat"], name: str, meows: bool)
# TODO: Create CatModel (pet_type: Literal["cat"], name: str, meows: bool)

# TODO: DogModel を作成してください (pet_type: Literal["dog"], name: str, barks: bool)
# TODO: Create DogModel (pet_type: Literal["dog"], name: str, barks: bool)

# TODO: Annotated と Field(discriminator="pet_type") を使って Pet 型を定義してください
# TODO: Define Pet type using Annotated and Field(discriminator="pet_type")

# TODO: POST /pets/ エンドポイントを実装してください
# TODO: Implement POST /pets/ endpoint
