from django.http import HttpResponse
from django.views import View
from prometheus_client import generate_latest, Counter

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

my_counter = Counter(
    'test_counter',
    'My first counter!'
)


class MetricsView(View):
    def get(self, request):

        my_counter.inc()

        return HttpResponse(
            generate_latest(),
            content_type='text/plain; version=0.0.4; charset=utf-8'
        )



