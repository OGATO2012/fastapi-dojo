from fastapi import FastAPI, Form, HTTPException

app = FastAPI()


@app.post("/register")
async def register(
    username: str = Form(...),
    email: str = Form(...),
    age: int = Form(...),
):
    errors = []
    if len(username) < 3:
        errors.append("username must be at least 3 characters")
    if "@" not in email:
        errors.append("email must contain @")
    if age < 18:
        errors.append("age must be 18 or older")
    if errors:
        raise HTTPException(status_code=422, detail=errors)
    return {"username": username, "email": email, "age": age}
