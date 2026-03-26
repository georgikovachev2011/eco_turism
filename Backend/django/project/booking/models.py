from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField()
    date_start = models.DateField()
    date_end = models.DateField()
    hotel_num = models.IntegerField()
    id = models.AutoField(primary_key=True)

