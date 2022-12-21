from django.contrib import admin
from .models import Nosotras, Equipo

# Register your models here.
class NosotrasAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'editado')

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)
    list_display =('nombre','apellido', 'activo', 'fecha', 'cargo')
    ordering = ('cargo',)
    search_fields = ('nombre',)
admin.site.register(Nosotras, NosotrasAdmin)
admin.site.register(Equipo, EquipoAdmin)