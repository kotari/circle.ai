from fastapi import FastAPI

from circle_ai.routes.ollama_api import router as OllamRouter


api_app = FastAPI()
api_app.include_router(OllamRouter, prefix="/ollama")


@api_app.get("/healthcheck")
async def healthcheck():
    """
    Endpoint for healthcheck
    """
    return {"status": 200}