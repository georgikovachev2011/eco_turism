from django.db import models

from django.db import models    
class Destination_Pages(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    long_description = models.CharField(max_length=128)
    rating = models.FloatField()
    reviews = models.IntegerField()
    num_of_guests = models.IntegerField()
    dollars_per_night = models.IntegerField()
    activities = models.CharField()
    amenities = models.CharField()
class Items(models.Model):
    destination_Pages = models.ForeignKey(Destination_Pages, on_delete=models.CASCADE)


