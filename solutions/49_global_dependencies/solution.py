from fastapi import FastAPI, Depends, HTTPException, Header


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app = FastAPI(dependencies=[Depends(verify_token)])


@app.get("/items/")
def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


@app.get("/users/")
def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
