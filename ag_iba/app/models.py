from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=160)
    adress = models.CharField(max_length=160)
    local = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=8)
    nif = models.CharField(max_length=9)
    added = models.DateTimeField(auto_now_add=True)

class Tax(models.Model):
    client = models.ForeignKey(Client)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=8)
    plate_date = models.DateField()

