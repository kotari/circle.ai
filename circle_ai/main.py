# circle.ai is a proxy service for various llm models

from fastapi import FastAPI
from circle_ai.routes import ollama_api, tgi_api

app = FastAPI()
app.title = "circle.ai"
app.description = "Proxy Service to front various LLM Models"

api = FastAPI(root_path="/api")
api.include_router(ollama_api.router, prefix="/ollama")
api.include_router(tgi_api.router, prefix="/hf")

app.mount("/api", api, name="api")


@api.get("/healthcheck")
async def healthcheck():
    """
    Endpoint for healthcheck
    """
    return {"status": 200}
