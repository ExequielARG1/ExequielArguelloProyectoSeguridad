from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='img/', default='img/default.png')
    
    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    descripcion = models.TextField()
    horarios = models.TextField()
    foto = models.ImageField(upload_to='img/fotos-sucursal/', default='img/fotos-sucursal/default-base')
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

class AcercaDe(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='img/avatars/', default='img/avatars/default-avatar.jpg')
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="customuser_set",
        related_query_name="user",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_set",
        related_query_name="user",
    )
    
#Aca vemos si se modifico o elimino a la persona para eliminar la foto
@receiver(post_delete, sender=Personal)
def delete_upload(sender, instance, **kwargs):
    if instance.foto:
        if default_storage.exists(instance.foto.name):
            default_storage.delete(instance.foto.name)

@receiver(pre_save, sender=Personal)
def delete_previous_file_on_change(sender, instance, **kwargs):
    # Si el ID del objeto no está definido, es un objeto nuevo, por lo que no tiene foto anterior
    if not instance.pk:
        return

    try:
        old_instance = Personal.objects.get(pk=instance.pk)
    except Personal.DoesNotExist:
        return

    # Si la foto ha cambiado
    if not old_instance.foto == instance.foto:
        if default_storage.exists(old_instance.foto.name):
            default_storage.delete(old_instance.foto.name)

@receiver(post_delete, sender=Sucursal)
def delete_upload_sucursal(sender, instance, **kwargs):
    if instance.foto:
        if default_storage.exists(instance.foto.name):
            default_storage.delete(instance.foto.name)

@receiver(pre_save, sender=Sucursal)
def delete_previous_file_on_change_sucursal(sender, instance, **kwargs):
    # Si el ID del objeto no está definido, es un objeto nuevo, por lo que no tiene foto anterior
    if not instance.pk:
        return

    try:
        old_instance = Sucursal.objects.get(pk=instance.pk)
    except Sucursal.DoesNotExist:
        return

    # Si la foto ha cambiado
    if not old_instance.foto == instance.foto:
        if default_storage.exists(old_instance.foto.name):
            default_storage.delete(old_instance.foto.name)

@receiver(post_delete, sender=CustomUser)
def delete_upload(sender, instance, **kwargs):
    if instance.avatar:
        if default_storage.exists(instance.avatar.name) and instance.avatar.name != 'img/avatars/default-avatar.jpg':
            default_storage.delete(instance.avatar.name)

@receiver(pre_save, sender=CustomUser)
def delete_previous_file_on_change(sender, instance, **kwargs):
    # Si el ID del objeto no está definido, es un objeto nuevo, por lo que no tiene avatar anterior
    if not instance.pk:
        return

    try:
        old_instance = CustomUser.objects.get(pk=instance.pk)
    except CustomUser.DoesNotExist:
        return

    # Si el avatar ha cambiado
    if not old_instance.avatar == instance.avatar:
        if default_storage.exists(old_instance.avatar.name) and old_instance.avatar.name != 'img/avatars/default-avatar.jpg':
            default_storage.delete(old_instance.avatar.name)
