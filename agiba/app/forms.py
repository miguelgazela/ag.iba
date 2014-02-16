from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.models import Client
from app.models import Tax
from datetime import date
import re

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'local', 'city', 
            'postal', 'nif', 'from_home']


    def clean_nif(self):
        data = self.cleaned_data['nif']
        try:
            digits = map(int, data)
        except ValueError:
            raise forms.ValidationError("Invalid NIF/NIPC")
       
        # NIF checksum algorithm
        control = digits[0] * 9
        for i in xrange(2,9):
            control += digits[i-1] * (10-i)
        control = 11 - (control % 11)
        if control >= 10:
            control = 0

        if control == digits[8]:
            return data
        raise forms.ValidationError("Invalid NIF/NIPC")


    def clean_postal(self):
        data = self.cleaned_data['postal']
        if re.search(r'^\d{4}([\-]\d{3})?$', data):
            return data
        raise forms.ValidationError('This postal code is invalid')

class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = '__all__'

    def clean_plate(self):
        """Validates the plate of the tax"""
        plate = self.cleaned_data['plate']
        if re.search(r'^(\d{2}-\d{2}-[a-zA-Z]{2})|(\d{2}-[a-zA-Z]{2}-\d{2})|([a-zA-Z]{2}-\d{2}-\d{2})$', plate):
            return plate.upper()
        raise forms.ValidationError('Invalid licence plate')

    def clean_plate_date(self):
        """Validates the date of the tax plate"""
        plate_date = self.cleaned_data['plate_date']
        if plate_date <= date.today():
            return plate_date
        raise forms.ValidationError('Invalid plate date')

    def clean_limit_date(self):
        """Validates the limit date of the tax payment"""
        plate_date = self.cleaned_data['plate_date']
        limit_date = self.cleaned_data['limit_date']

        if limit_date > plate_date and limit_date.month == plate_date.month:
            return limit_date
        raise forms.ValidationError('Invalid limit date for payment')

