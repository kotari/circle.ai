from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from ollama import RequestError, ResponseError


OLLAMA_EXCEPTIONS = (RequestError, ResponseError)


class OllamaRouteExceptionHandler(APIRoute):
    """
    This is a route class override for the Ollama router. It is used to
    catch common exceptions that are raised by the Ollama API and return an
    internal server error response with its associated error message.
    """

    def get_route_handler(self):
        original_route_handler = super().get_route_handler()

        async def exception_handler(request: Request) -> JSONResponse:
            """
            Catch Ollama exceptions and return an internal server error response.

            :param request: The request object
            :type request: Request
            :return: Response or Internal server error response with error message
            :rtype: JSONResponse
            """
            try:
                response = await original_route_handler(request)
            except OLLAMA_EXCEPTIONS as e:
                # print exception traceback to console
                # logger.exception(type(e), e, e.__traceback__)
                print(e)
                raise HTTPException(
                    status_code=500,
                    detail=str(e),
                )
            return response

        return exception_handler
