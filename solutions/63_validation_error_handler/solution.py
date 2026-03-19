from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

validation_errors_log = []

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    validation_errors_log.append({
        "path": str(request.url.path),
        "error_count": len(exc.errors())
    })
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation Error",
            "errors": exc.errors(),
            "body": str(exc.body) if exc.body else None
        }
    )

class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

@app.post("/products/")
def create_product(product: Product):
    return product

@app.get("/error-log")
def get_error_log():
    return validation_errors_log
