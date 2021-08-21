from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, models

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class meta:
        model = User
        fields = ['username','email','password1','password2']
