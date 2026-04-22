from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from inicio import views
from servicios import views as views_servicios


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.nosotros, name="nosotros"),
    path('servicios/', views_servicios.servicios, name="servicios"),
    path('proyectosrealizados/', views_servicios.proyecto, name="proyectosrealizados"),
    path('registrar/', views_servicios.registrar, name="Registrar"),
    path('cotizacion/<int:id>/', views_servicios.cotizacion, name='cotizacion'),
    path('contacto/', views_servicios.contacto, name='Contacto'),
    path('video1/', views_servicios.video1, name='video1'), 
    path('video2/', views_servicios.video2, name='video2'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    if hasattr(settings, 'STATICFILES_DIRS'):
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])