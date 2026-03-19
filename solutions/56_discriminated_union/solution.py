from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Literal, Annotated
from pydantic import Field

app = FastAPI()

class CatModel(BaseModel):
    pet_type: Literal["cat"]
    name: str
    meows: bool

class DogModel(BaseModel):
    pet_type: Literal["dog"]
    name: str
    barks: bool

Pet = Annotated[Union[CatModel, DogModel], Field(discriminator="pet_type")]

@app.post("/pets/")
def create_pet(pet: Pet):
    return pet
