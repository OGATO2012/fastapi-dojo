from fastapi import FastAPI, APIRouter

app = FastAPI()

# TODO: admin_router を作成してください
# GET /stats → {"stats": "admin stats data"}
# DELETE /cache → {"message": "cache cleared"}
# TODO: Create admin_router
# GET /stats → {"stats": "admin stats data"}
# DELETE /cache → {"message": "cache cleared"}

# TODO: public_router を作成してください
# GET /info → {"info": "public info"}
# GET /status → {"status": "ok"}
# TODO: Create public_router
# GET /info → {"info": "public info"}
# GET /status → {"status": "ok"}

# TODO: admin_router を prefix="/admin", tags=["admin"] で app に include してください
# TODO: public_router を prefix="/public", tags=["public"] で app に include してください
# TODO: Include admin_router with prefix="/admin", tags=["admin"]
# TODO: Include public_router with prefix="/public", tags=["public"]
