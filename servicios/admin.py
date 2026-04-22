from django.contrib import admin
from .models import Proyecto
from django.shortcuts import redirect
from django.urls import reverse
from .models import Servicio
from .models import Resena
from .models import Respuesta
from .models import Cotizacion
from .models import Descripcion


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('folio', 'proyecto', 'empresa', 'descripcion')
    search_fields = ('folio', 'proyecto', 'empresa', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('proyecto', 'empresa')

admin.site.register(Proyecto, AdministrarModelo)


class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'created'
    list_filter = ('nombre',)

admin.site.register(Servicio, ServicioAdmin)


class AdministrarRespuesta(admin.ModelAdmin):
    readonly_fields = ('created', 'id')  
    list_display = ('id', 'cotizacion', 'created')
    search_fields = ('mensaje',)  
    date_hierarchy = 'created'

admin.site.register(Respuesta, AdministrarRespuesta)


class ResenaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensaje', 'servicio', 'calificacion')
    search_fields = ('usuario', 'mensaje')
    list_filter = ('servicio',)

admin.site.register(Resena, ResenaAdmin)


class CotizacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # ✔ coma IMPORTANTE
    list_display = ('nombre', 'correo', 'servicio')
    search_fields = ('nombre', 'correo')
    list_filter = ('nombre', 'servicio')

admin.site.register(Cotizacion, CotizacionAdmin)

class DescripcionAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)  # No se puede editar la fecha de creación
    list_display = ('servicio', 'descripcion', 'created')  # Columnas visibles
    search_fields = ('servicio', 'descripcion')  # Campos por los que se puede buscar
    list_filter = ('servicio',)  # Filtro lateral por servicio
    date_hierarchy = 'created'  # Navegación por fecha de creación

# Registrar el modelo con su admin
admin.site.register(Descripcion, DescripcionAdmin)