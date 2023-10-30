from django.contrib import admin
from .models import Personal, Sucursal, AcercaDe, CustomUser, Contact

# Registrar el modelo Personal
@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'puesto', 'descripcion']
    search_fields = ['nombre', 'puesto']
    list_filter = ['puesto']

# Registrar el modelo Sucursal
@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'horarios', 'ubicacion']
    search_fields = ['descripcion', 'ubicacion']
    list_filter = ['ubicacion']

# Registrar el modelo AcercaDe
@admin.register(AcercaDe)
class AcercaDeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']
    search_fields = ['titulo']

# Registrar el modelo CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_active']

# Registrar el modelo Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email']

