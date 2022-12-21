from django.db import models
from django.utils import timezone

# Create your models here.
class Testimonios(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    profesion = models.CharField(max_length=50, null=True, blank=True)
    texto = models.TextField(max_length=280, null=False)
    activo = models.BooleanField(default=True)
    publicado = models.DateField(default=timezone.now())
    
    class Meta:
        verbose_name = "testimonio"
        verbose_name_plural = "testimonios"
        ordering =['-publicado']

    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        super().delete()