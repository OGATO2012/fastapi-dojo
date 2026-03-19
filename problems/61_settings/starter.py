from fastapi import FastAPI
from pydantic_settings import BaseSettings
from functools import lru_cache

# TODO: Settings クラスを作成してください (BaseSettings を継承)
# TODO: Create Settings class (inheriting from BaseSettings)
# Fields: app_name, debug, api_version, max_items
# Config.env_prefix = "APP_"

# TODO: @lru_cache() で get_settings() 関数を作成してください
# TODO: Create get_settings() function with @lru_cache()

app = FastAPI()

# TODO: GET /settings エンドポイントを実装してください
# TODO: Implement GET /settings endpoint
