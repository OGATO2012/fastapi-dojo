import time
from fastapi import FastAPI, Request

app = FastAPI()

# TODO: リクエスト処理時間を計測するミドルウェアを追加してください
# X-Process-Time ヘッダーにかかった時間 (秒, 小数点以下4桁) を設定する
# TODO: Add middleware to measure request processing time
# Set X-Process-Time header to elapsed seconds (4 decimal places)

# TODO: GET /slow エンドポイントを実装してください
# クエリパラメータ delay: float (デフォルト 0.1) 秒スリープする
# {"message": "slow response", "delay": delay} を返す
# TODO: Implement GET /slow
# Sleep for delay: float (default 0.1) seconds
# Return {"message": "slow response", "delay": delay}

# TODO: GET /fast エンドポイントを実装してください
# すぐに {"message": "fast response"} を返す
# TODO: Implement GET /fast
# Return {"message": "fast response"} immediately
