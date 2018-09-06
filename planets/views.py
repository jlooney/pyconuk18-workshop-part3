from rest_framework import generics
from planets.serializers import PlanetSerializer
from planets.models import Planet


class PlanetList(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class SinglePlanet(generics.RetrieveDestroyAPIView):
    serializer_class = PlanetSerializer
    lookup_field = 'name'
    queryset = Planet.objects.all()
