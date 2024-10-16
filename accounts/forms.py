from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms

class CustomUserCreationForn(UserCreationForm):
    class Meta:
        model=User
        fields=['Username','email','password1','password2']
