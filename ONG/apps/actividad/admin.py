from django.contrib import admin
from .models import Actividad

# Register your models here.

class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'publicado')
    list_display =('titulo','id', 'activo', 'fecha')
    ordering = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Actividad, ActividadAdmin)