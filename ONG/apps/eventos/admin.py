from django.contrib import admin
from .models import Eventos

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'publicado')
    list_display =('titulo','id', 'activo', 'fecha')
    ordering = ('fecha',)
    search_fields = ('titulo',)

admin.site.register(Eventos, EventosAdmin)