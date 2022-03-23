from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200,
        verbose_name="Titulo")
    number = models.IntegerField(
        verbose_name="Número")
    content = models.TextField(
        verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",
        upload_to="services")
    icon = models.ImageField(verbose_name="Icono",
        upload_to="services")
    classAdded = models.CharField(max_length=200,
        verbose_name="Clase añadida",
        default="claseaañadir")
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title