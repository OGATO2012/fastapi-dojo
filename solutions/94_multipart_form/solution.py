from fastapi import FastAPI, Form, UploadFile, File

app = FastAPI()


@app.post("/upload")
async def upload(
    name: str = Form(...),
    description: str = Form(default=""),
    file: UploadFile = File(...),
):
    return {
        "name": name,
        "description": description,
        "filename": file.filename,
        "content_type": file.content_type,
    }
