from django.db import models
from rest_framework import serializers

class ListDestinationsPagesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=50)
    long_description = serializers.CharField(max_length=256)
    rating = serializers.FloatField()
    reviews = serializers.IntegerField()
    num_of_guests = serializers.IntegerField()
    dollars_per_night = serializers.IntegerField()
    activities = serializers.CharField()
    amenities = serializers.CharField()
    images = serializers.SerializerMethodField()
    id = serializers.IntegerField()


    def get_images(self, obj):
        return [f"/Images/{obj.id}/{i}"for i in range(1,5)]
    
class DestinationPageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
