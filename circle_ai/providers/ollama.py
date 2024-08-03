from ollama import Client
from typing import Optional, Iterator
from circle_ai.utils.stream_processor import StreamProcessor
from ollama import GenerateResponse


OLLAMA_ENDPOINTS = ["generate", "chat"]


class OllamaWrapper:
    def __init__(self) -> None:
        self.ollama_client = Client(host="http://rajesh-MS-7C79:11434")

    def _validate_ollama_endpoint(self, endpoint: str) -> None:
        if endpoint not in OLLAMA_ENDPOINTS:
            raise NotImplementedError(
                f"ollama endpoint must be one of `{OLLAMA_ENDPOINTS}"
            )

    def _call_generate_endpoint(
        self,
        model: str = "llama2",
        prompt: str = "why is the sky blue?",
        stream: bool = False,
        **kwargs,
    ):
        resp = self.ollama_client.generate(model, prompt, stream=stream, **kwargs)
        return resp

    def send_ollama_request(
        self,
        endpoint: str,
        model: Optional[str] = None,
        prompt: Optional[str] = None,
        stream: bool = False,
        **kwargs,
    ):
        self._validate_ollama_endpoint(endpoint)

        if endpoint == "generate":
            result = self._call_generate_endpoint(model, prompt, stream)

        if not stream:
            cached_response = result
        else:
            stream_processor = StreamProcessor(stream_processor=stream_generator_ollama)
            ollama_response = stream_processor.process_stream(result)
            cached_response = stream_processor.get_cached_streamed_response()

        return cached_response


def stream_generator_ollama(generator: Iterator) -> Iterator[str]:
    resp: dict
    for resp in generator:
        yield resp["response"]
