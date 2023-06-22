from http import HTTPStatus

from rest_framework.views import Response, exception_handler


def api_exception_handler(exc: Exception, context: dict) -> Response:
    """
    a custom excepterion handler with more detailed information.
    {
        "error": {
            "status_code": 404,
            "message":"",
            "detail":[]
        }
    }

    """

    response = exception_handler(exc, context)
    if response is not None:
        http_code_to_message = {v.value: v.phrase for v in HTTPStatus}
        payload = {
            "status_code": response.status_code,
            "message": http_code_to_message[response.status_code],
            "detail": response.data,
        }
        response.data = {"error": payload}

    return response
