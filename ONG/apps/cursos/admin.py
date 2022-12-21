from django.contrib import admin
from .models import Cursos

# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'publicado')
    list_display =('titulo','id', 'activo', 'fecha')
    ordering = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Cursos, CursosAdmin)

# Register your models here.
