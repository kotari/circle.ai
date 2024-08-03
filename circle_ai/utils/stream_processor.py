from typing import List, Iterator, Callable


class StreamProcessor:
    def __init__(self, stream_processor: Callable) -> None:
        self.stream_processor = stream_processor
        self.cached_streamed_response = []

    def process_stream(self, response: Iterator) -> Iterator:
        for item in self.stream_processor(response):
            self.cached_streamed_response.append(item)
            # yield item

    def get_cached_streamed_response(self) -> List[str]:
        return self.cached_streamed_response
