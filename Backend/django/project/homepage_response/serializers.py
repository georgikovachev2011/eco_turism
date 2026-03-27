from django.db import models
from rest_framework import serializers

class ListDestinationsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=50)
    short_description = serializers.CharField(max_length=128)
    rating = serializers.FloatField()
    reviews = serializers.IntegerField()
    num_of_guests = serializers.IntegerField()
    dollars_per_night = serializers.IntegerField()