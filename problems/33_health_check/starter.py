from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

start_time = datetime.utcnow()

# TODO: GETエンドポイント /health を実装してください
# - status: "healthy" を返す
# - timestamp: 現在のUTC時刻をISO形式の文字列で返す
# - uptime_seconds: アプリ起動からの経過秒数を返す
#
# TODO: Implement GET /health endpoint
# - Return status: "healthy"
# - Return timestamp: current UTC time as ISO format string
# - Return uptime_seconds: seconds elapsed since app start
