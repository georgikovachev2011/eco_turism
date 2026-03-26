from django.db import models

class Sign_up(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField()

 