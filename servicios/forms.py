from django import forms
from .models import Resena, Servicio

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['usuario', 'mensaje']