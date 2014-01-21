from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=160)
    address = models.CharField(max_length=160)
    local = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.CharField(max_length=8)
    nif = models.CharField(max_length=9)
    added = models.DateTimeField(auto_now_add=True)
    from_home = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.name

class Tax(models.Model):
    client = models.ForeignKey(Client)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate = models.CharField(max_length=8)
    plate_date = models.DateField()
    limit_date = models.DateField(default=datetime.now())

    @property
    def days_left(self):
        # temporary
        return 10


