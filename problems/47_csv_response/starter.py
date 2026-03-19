from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

# TODO: Create GET /export/csv endpoint that:
#   - Builds CSV string with header "id,name,price" and at least 3 data rows
#   - Returns Response with:
#     - content = csv_data string
#     - media_type = "text/csv"
#     - headers = {"Content-Disposition": "attachment; filename=items.csv"}
# TODO: GET /export/csvエンドポイントを作成する:
#   - ヘッダー"id,name,price"と少なくとも3行のデータを持つCSV文字列を作成する
#   - 以下でResponseを返す:
#     - content = csv_data文字列
#     - media_type = "text/csv"
#     - headers = {"Content-Disposition": "attachment; filename=items.csv"}
