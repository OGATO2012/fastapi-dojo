from fastapi import FastAPI, APIRouter

app = FastAPI()

admin_router = APIRouter()
public_router = APIRouter()


@admin_router.get("/stats")
async def admin_stats():
    return {"stats": "admin stats data"}


@admin_router.delete("/cache")
async def clear_cache():
    return {"message": "cache cleared"}


@public_router.get("/info")
async def public_info():
    return {"info": "public info"}


@public_router.get("/status")
async def public_status():
    return {"status": "ok"}


app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(public_router, prefix="/public", tags=["public"])
