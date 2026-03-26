from django.db import models

class Signup(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    
