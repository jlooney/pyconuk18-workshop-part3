from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    diameter = models.FloatField()  # in km
    distance_from_sun = models.FloatField()  # in km
    number_of_moons = models.IntegerField()

