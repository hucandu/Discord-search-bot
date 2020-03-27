from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from . import error_codes
from . import renderers


class MyOperatorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def _get_statuscode_from_exception(self, exception):
        statuscode_exceptions = {
            TypeError: 500,
            KeyError: 500,
        }

        return statuscode_exceptions.get(exception.__class__, 500)


    def process_exception(self, request, exception):
        status_code = self._get_statuscode_from_exception(exception)
        response = Response({
            "errors": {"detail": str(exception)},
            "code": error_codes.SERVER_ERROR
        }, status_code)
        response.accepted_media_type = "application/json"
        response.renderer_context = {}

        response.accepted_renderer = renderers.MyOperatorRenderer()
        return response
