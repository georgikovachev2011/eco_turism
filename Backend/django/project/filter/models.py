from django.db import models

class Filter_options(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('eco_house'),
        ('guest_house'),
        ('traditional_home'),
        ('all_types'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price_per_night = models.IntegerField()  
def __str__(self):
        return self.name