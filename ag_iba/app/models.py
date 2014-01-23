# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date

class Client(models.Model):
    name = models.CharField(max_length=160, verbose_name='Nome')
    address = models.CharField(max_length=160, verbose_name="Morada")
    local = models.CharField(max_length=100, verbose_name="Localidade")
    city = models.CharField(max_length=100, verbose_name="Cidade")
    postal = models.CharField(max_length=8, verbose_name="Código postal")
    nif = models.CharField(max_length=9, unique=True, verbose_name="NIF/NIPC")
    added = models.DateTimeField(auto_now_add=True)
    from_home = models.BooleanField(default=False, blank=True, verbose_name="Casa")

    class Meta:
        verbose_name = 'Cliente'

    def __unicode__(self):
        return self.name

    def has_taxes_this_month(self):
        taxes = self.tax_set.all()
        for tax in taxes:
            if tax.this_month():
                return True
        return False

class Tax(models.Model):
    client = models.ForeignKey(Client, verbose_name="Cliente")
    brand = models.CharField(max_length=100, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    plate = models.CharField(max_length=8, verbose_name="Matrícula")
    plate_date = models.DateField(verbose_name="Data Matrícula")
    limit_date = models.DateField(default=datetime.now(), verbose_name="Data Limite de Pagamento")

    class Meta:
        verbose_name = "Imposto"

    def __unicode__(self):
        return "{brand} {model}".format(
            brand=self.brand,
            model=self.model
        )
        

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

    def this_month(self):
        today = date.today()
        if today.year == self.limit_date.year:
            return today.month == self.limit_date.month

    def next_month(self):
        today = date.today()
        if today.year == self.limit_date.year:
            return self.limit_date.month == (today.month + 1)






