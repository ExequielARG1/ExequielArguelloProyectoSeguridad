from django import forms
from .models import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre', 'puesto','descripcion', 'foto']  # Asegúrate de que uses 'foto' en lugar de 'imagen'
