from fastapi import FastAPI
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = False
    api_version: str = "1.0"
    max_items: int = 100

    class Config:
        env_prefix = "APP_"

@lru_cache()
def get_settings():
    return Settings()

app = FastAPI()

@app.get("/settings")
def read_settings():
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "api_version": settings.api_version,
        "max_items": settings.max_items,
    }
