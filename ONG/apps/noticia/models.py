from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#----------noticias
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    editado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering =['-creado']

    def __str__(self):
        return self.nombre

class Noticias(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    introduccion = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=False, blank=True, upload_to='noticia', default='noticia/default.png')
    publicado = models.DateField(default=timezone.now())
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering =['-publicado']

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.delete(self.imagen.name)
        super().delete()

    
class Comentarios(models.Model): 
    noticia = models.ForeignKey(Noticias, on_delete=models.SET_NULL, related_name='comments', null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    publicado = models.DateField(default=timezone.now())
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        ordering =['-publicado']

    def __str__(self):
        return '%s - %s' % (self.author.username, self.noticia.titulo)
    
 