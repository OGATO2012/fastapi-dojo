from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class Cat(BaseModel):
    type: str = "cat"
    name: str
    indoor: bool


class Dog(BaseModel):
    type: str = "dog"
    name: str
    breed: str


@app.post("/animals/")
def create_animal(animal: Union[Cat, Dog]):
    return animal


@app.get("/pets/")
def get_pets() -> list[Union[Cat, Dog]]:
    return [
        Cat(name="Whiskers", indoor=True),
        Dog(name="Rex", breed="German Shepherd"),
    ]
