from fastapi import FastAPI

# TODO: Create FastAPI app with custom OpenAPI metadata:
#   - title="My Awesome API"
#   - description with markdown (e.g., "This is a **custom** FastAPI application...")
#   - version="2.0.0"
#   - contact={"name": "API Support", "email": "support@example.com"}
#   - license_info={"name": "MIT"}
# TODO: カスタムOpenAPIメタデータを持つFastAPIアプリを作成する:
#   - title="My Awesome API"
#   - マークダウンを含むdescription（例: "This is a **custom** FastAPI application..."）
#   - version="2.0.0"
#   - contact={"name": "API Support", "email": "support@example.com"}
#   - license_info={"name": "MIT"}

app = FastAPI()

# TODO: Create GET / returning {"message": "Check /docs for custom OpenAPI"}
# TODO: {"message": "Check /docs for custom OpenAPI"}を返すGET /を作成する
