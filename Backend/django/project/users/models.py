from django.db import models
from django.db import models

class Userdata(models.Model):
    username = models.CharField()
    email = models.EmailField()
    password = models.CharField()
    code = models.CharField(null=True)
