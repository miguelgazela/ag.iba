from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date

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

    def __unicode__(self):
        return "Cliente: {client} - {brand} {model}".format(
            client=self.client.name, 
            brand=self.brand,
            model=self.model
        )

    @property
    def days_left(self):
        limit = date(
            self.limit_date.year, 
            self.limit_date.month,
            self.limit_date.day
        )
        diff = limit - date.today()
        
        # when the limit is overdue
        if diff.days < 0:
            return 0
        return diff.days

    @property
    def this_month(self):
        today = date.today()
        if today.year == self.limit_date.year:
            return today.month == self.limit_date.month

    @property
    def next_month(self):
        today = date.today()
        if today.year == self.limit_date.year:
            return self.limit_date.month == (today.month + 1)






