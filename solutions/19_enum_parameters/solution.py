from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


MESSAGES = {
    ModelName.alexnet: "Deep Learning FTW!",
    ModelName.resnet: "Have some residuals!",
    ModelName.lenet: "LeCNN all the images",
}


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return {"model_name": model_name.value, "message": MESSAGES[model_name]}
