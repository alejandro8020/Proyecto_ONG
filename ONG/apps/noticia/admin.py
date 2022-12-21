from django.contrib import admin
from .models import Noticias, Categoria, Comentarios
# Register your models here.

'''@admin.register(Noticias)
class AuthorAdmion(admin.ModelAdmin):
    readonly_fields = ('fecha', 'publicado')
    list_display =('titulo','id', 'activo', 'fecha', 'categoria')'''
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')

class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'publicado')
    list_display =('titulo','id', 'activo', 'fecha', 'categoria')
    ordering = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticias, NoticiaAdmin)
admin.site.register(Comentarios)