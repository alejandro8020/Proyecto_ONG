from django.db import models
from django.utils import timezone

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    introduccion = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=False, blank=True, upload_to='eventos', default='noticia/default.png')
    publicado = models.DateField(default=timezone.now())
    
    class Meta:
        verbose_name = "eventos"
        verbose_name_plural = "eventos"
        ordering =['-publicado']

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()