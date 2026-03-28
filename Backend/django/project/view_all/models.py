from django.db import models    
class View_All_destinations(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    short_description = models.CharField(max_length=128)
    rating = models.FloatField()
    reviews = models.IntegerField()
    num_of_guests = models.IntegerField()
    dollars_per_night = models.IntegerField()

class Items(models.Model):
    all_destinations = models.ForeignKey(View_All_destinations, on_delete=models.CASCADE)
 
