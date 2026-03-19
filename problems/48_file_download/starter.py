from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

# TODO: Create GET /download/report.txt endpoint that:
#   - Creates a text content string (e.g., a report with multiple lines)
#   - Returns Response with:
#     - content = the text string
#     - media_type = "text/plain"
#     - headers = {"Content-Disposition": "attachment; filename=report.txt"}
# TODO: GET /download/report.txtエンドポイントを作成する:
#   - テキストコンテンツ文字列を作成する（複数行のレポートなど）
#   - 以下でResponseを返す:
#     - content = テキスト文字列
#     - media_type = "text/plain"
#     - headers = {"Content-Disposition": "attachment; filename=report.txt"}
