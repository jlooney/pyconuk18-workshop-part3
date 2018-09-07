from prometheus_client import Counter

requests_total = Counter(
    'django_http_requests_total',
    'Total count of requests',
    ['view'])

class PrometheusMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        requests_total.labels(view_func.__name__).inc()

