from django import forms
from .models import *

class placesForm(forms.ModelForm):
    class Meta:
        model = Places
        fields= '__all__'