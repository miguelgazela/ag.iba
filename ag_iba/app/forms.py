from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_email(self):
        data = self.cleaned_data['email']
        return data
