import uuid
from fastapi import FastAPI, Depends

app = FastAPI()

_config = {"app_name": "FastAPI Dojo", "version": "1.0.0", "debug": False}


def get_request_id() -> str:
    return str(uuid.uuid4())


def get_config() -> dict:
    return _config


@app.get("/info")
async def get_info(
    request_id: str = Depends(get_request_id),
    config: dict = Depends(get_config),
    config2: dict = Depends(get_config),
):
    return {
        "request_id": request_id,
        "config": config,
        "same_config": config is config2,
    }
