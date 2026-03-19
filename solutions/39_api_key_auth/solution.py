from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

app = FastAPI()

API_KEY = "my-secret-api-key"
api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key


@app.get("/protected")
def protected_route(api_key: str = Security(verify_api_key)):
    return {"message": "Access granted", "api_key": api_key}
