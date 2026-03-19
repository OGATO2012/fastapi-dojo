from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(
    item_id: Annotated[str, Path(pattern=r"^[a-z]{3}-[0-9]{3}$")]
):
    return {"item_id": item_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
