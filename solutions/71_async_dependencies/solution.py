from fastapi import Depends, FastAPI

app = FastAPI()


async def get_db():
    return {"status": "connected", "host": "localhost"}


@app.get("/data")
async def get_data(db: dict = Depends(get_db)):
    return {"db": db["status"], "data": [1, 2, 3]}


@app.get("/health")
async def get_health(db: dict = Depends(get_db)):
    return {"status": "ok", "db_host": db["host"]}
