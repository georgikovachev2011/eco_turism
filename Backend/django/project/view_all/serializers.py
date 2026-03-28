from django.db import models
from rest_framework import serializers

class ViewAllDestinationsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    location = serializers.CharField(max_length=50)
    short_description = serializers.CharField(max_length=128)
    rating = serializers.FloatField()
    reviews = serializers.IntegerField()
    dollars_per_night = serializers.IntegerField()
    image = serializers.SerializerMethodField()
    num_of_guests = serializers.IntegerField()
    id = serializers.IntegerField()

    def get_image(self, obj):
        return f"../static/Images/{obj.id}/1.jpg"