from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/submit")
def submit_form(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}
