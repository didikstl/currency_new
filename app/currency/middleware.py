from time import time
from app.currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_type = request.method
        request.request_type = request_type
        request_path = request.path
        request.request_path = request_path

        start = time()

        response = self.get_response(request)

        end = time()
        print(f'After in middleware {end - start}, {request_type}, {request_path}')

        RequestResponseLog.objects.create(
            path=request_path,
            request_method=request_type,
            time=(end - start)
        )

        return response
