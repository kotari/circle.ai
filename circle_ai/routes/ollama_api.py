from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse
from starlette.responses import JSONResponse
from circle_ai.exceptions import OllamaRouteExceptionHandler
from circle_ai.models import GenerateInput
from circle_ai.providers.ollama import OllamaWrapper

router = APIRouter(route_class=OllamaRouteExceptionHandler)


@router.post("/generate")
def generate(user_input: GenerateInput, background_tasks: BackgroundTasks) -> JSONResponse:
    wrapper = OllamaWrapper()
    resp = wrapper.send_ollama_request("generate", model=user_input.model, prompt=user_input.prompt, stream=user_input.stream)
    return resp