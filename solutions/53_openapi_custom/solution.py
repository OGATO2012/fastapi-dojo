from fastapi import FastAPI

app = FastAPI(
    title="My Awesome API",
    description="This is a **custom** FastAPI application with customized OpenAPI docs.",
    version="2.0.0",
    contact={"name": "API Support", "email": "support@example.com"},
    license_info={"name": "MIT"},
)


@app.get("/")
def root():
    return {"message": "Check /docs for custom OpenAPI"}
