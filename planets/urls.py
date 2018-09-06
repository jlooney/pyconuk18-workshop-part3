from django.conf.urls import url
from planets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^planets', views.PlanetList.as_view()),
    url(r'^planet/(?P<name>[a-zA-Z]+)',
        views.SinglePlanet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
