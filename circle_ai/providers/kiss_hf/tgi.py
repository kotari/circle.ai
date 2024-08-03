# from ollama import Client
from typing import Optional, Iterator
from circle_ai.utils.stream_processor import StreamProcessor
from circle_ai.providers.kiss_hf.tgi_pipeline import pipe
import httpx

# from ollama import GenerateResponse


TGI_ENDPOINTS = ["generate"]


class TGIWrapper:
    def __init__(self) -> None:
        # I will be running tgi code using in pipeline and would not be communicating to an external host/endpoint
        self.host = "https://httpbin.org/"
        # This is for local development and testing
        self.pipe = pipe

    def _validate_tgi_endpoint(self, endpoint: str) -> None:
        if endpoint not in TGI_ENDPOINTS:
            raise NotImplementedError(f"tgi endpoint must be one of `{TGI_ENDPOINTS}")

    def _call_generate_endpoint(
        self,
        model: str = "llama2",
        prompt: str = "why is the sky blue?",
        stream: bool = False,
        **kwargs,
    ):
        # data = {}
        # data["prompt"] = prompt
        # data["model"] = model
        # data["parameters"] = {**kwargs}
        # resp = httpx.post(self.host + "post", data=data)
        # return resp.json()
        return pipe(prompt, **kwargs)

    def send_tgi_request(
        self,
        endpoint: str,
        model: Optional[str] = None,
        prompt: Optional[str] = None,
        stream: bool = False,
        **kwargs,
    ):
        self._validate_tgi_endpoint(endpoint)

        if endpoint == "generate":
            result = self._call_generate_endpoint(model, prompt, stream)

        if not stream:
            cached_response = result
        else:
            stream_processor = StreamProcessor(stream_processor=stream_generator_tgi)
            ollama_response = stream_processor.process_stream(result)
            cached_response = stream_processor.get_cached_streamed_response()

        return cached_response


def stream_generator_tgi(generator: Iterator) -> Iterator[str]:
    resp: dict
    for resp in generator:
        yield resp["response"]
