from django.contrib import admin
from .models import Testimonios

# Register your models here.
class TestimonioAdmin(admin.ModelAdmin):
    readonly_fields = ( 'publicado',)
    list_display =('nombre','id', 'activo', 'publicado')
    ordering = ('publicado',)
    search_fields = ('nombre',)

admin.site.register(Testimonios, TestimonioAdmin)