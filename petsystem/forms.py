from django import forms
from .models import Pets

class PestForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'location', 'image','age','likes','dislikes','contact']
