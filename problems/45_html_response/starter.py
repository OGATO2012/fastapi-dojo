from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# TODO: Create GET / endpoint with response_class=HTMLResponse that:
#   - Returns an HTMLResponse with an HTML page containing:
#     - <title>FastAPI HTML</title>
#     - <h1>Hello from FastAPI!</h1>
#     - A <p> paragraph element
#   - Status code 200
# TODO: response_class=HTMLResponseを設定したGET /エンドポイントを作成する:
#   - 以下を含むHTMLページのHTMLResponseを返す:
#     - <title>FastAPI HTML</title>
#     - <h1>Hello from FastAPI!</h1>
#     - <p>段落要素
#   - ステータスコード200
