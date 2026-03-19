from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# TODO: Create Cat(BaseModel) with fields:
#   - type: str = "cat"
#   - name: str
#   - indoor: bool
# TODO: 以下のフィールドを持つCat(BaseModel)を作成する:
#   - type: str = "cat"
#   - name: str
#   - indoor: bool

# TODO: Create Dog(BaseModel) with fields:
#   - type: str = "dog"
#   - name: str
#   - breed: str
# TODO: 以下のフィールドを持つDog(BaseModel)を作成する:
#   - type: str = "dog"
#   - name: str
#   - breed: str

# TODO: Create POST /animals/ that:
#   - Accepts animal: Union[Cat, Dog] in the request body
#   - Returns the animal
# TODO: POST /animals/を作成する:
#   - リクエストボディにanimal: Union[Cat, Dog]を受け取る
#   - animalを返す

# TODO: Create GET /pets/ that returns:
#   - A list containing Cat(name="Whiskers", indoor=True) and Dog(name="Rex", breed="German Shepherd")
# TODO: 以下を返すGET /pets/を作成する:
#   - Cat(name="Whiskers", indoor=True)とDog(name="Rex", breed="German Shepherd")を含むリスト
