from django.db import models

# Create your models here.
class Studies(models.Model):
    title = models.CharField(max_length=200,
        verbose_name="Título")
    subtitle = models.CharField(max_length=200,
        verbose_name="Subtítulo")
    content = models.TextField(
        verbose_name="Contenido")
    video = models.FileField(
        verbose_name="Vídeo",
        upload_to="studies")
    preview = models.ImageField(verbose_name="Preview",
        upload_to = "services", default=0)
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name="caso de estudio"
        verbose_name_plural="casos de estudios"
        ordering = ['-created']

    def __str__(self):
        return self.title
