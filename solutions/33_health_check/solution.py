from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

start_time = datetime.utcnow()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "uptime_seconds": (datetime.utcnow() - start_time).total_seconds(),
    }
