from django.db import models

class Personal(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='Hunter_App/img/', default='Hunter_App/img/default.png')
    def __str__(self):
        return self.nombre