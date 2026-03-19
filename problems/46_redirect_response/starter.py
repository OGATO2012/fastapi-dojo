from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

# TODO: Create GET /old-path endpoint that:
#   - Returns RedirectResponse(url="/new-path", status_code=301)
# TODO: GET /old-pathエンドポイントを作成する:
#   - RedirectResponse(url="/new-path", status_code=301)を返す

# TODO: Create GET /new-path endpoint that:
#   - Returns {"message": "You reached the new path"}
# TODO: GET /new-pathエンドポイントを作成する:
#   - {"message": "You reached the new path"}を返す
