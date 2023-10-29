from django.db import models
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
