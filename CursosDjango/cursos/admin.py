from django.contrib import admin
from .models import Curso
from .models import Actividad

class AdministrarModelo(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'duracion', 'precio', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('activo', 'fecha_creacion')
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')

admin.site.register(Curso, AdministrarModelo)


class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'desc')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Actividad, AdministrarActividad)