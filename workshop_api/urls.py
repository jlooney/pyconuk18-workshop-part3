from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from metrics import views as metrics_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('metrics$', metrics_views.MetricsView.as_view()),
    url(r'^', include('planets.urls'))
]
