from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


def event_generator():
    for i in range(1, 6):
        yield f"data: event {i}\n\n"


@app.get("/events")
def stream_events():
    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/status")
def status():
    return {"status": "ok"}
