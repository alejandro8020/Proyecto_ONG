from django.db import models


# Create your models here.
class Nosotras(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=50, null=False)
    contenido = models.TextField(verbose_name="Contenido", null=False)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Nos"
        verbose_name_plural = "Nosotras"
        ordering =['titulo']

    def __str__(self):
        return self.titulo

class Equipo(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    cargo = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=False, blank=True, upload_to='nosotras')
    
    class Meta:
        verbose_name = "equipo"
        verbose_name_plural = "equipos"
        ordering =['-nombre']

    def __str__(self):
        return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()