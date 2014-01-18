from django.contrib.auth.forms import UserCreationForm
from django import forms
from app.models import Client

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
        # validate the nif here
        return data