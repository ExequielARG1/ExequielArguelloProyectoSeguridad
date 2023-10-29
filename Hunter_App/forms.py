# forms.py
from django import forms
from .models import Personal, Sucursal, AcercaDe, CustomUser

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre', 'puesto', 'descripcion', 'foto']

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ['descripcion', 'horarios', 'foto', 'ubicacion']

class AcercaDeForm(forms.ModelForm):
    class Meta:
        model = AcercaDe
        fields = ['titulo', 'descripcion']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']