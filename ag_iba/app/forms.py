from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.models import Client
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
             # digits = [int(c) for c in data] or
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