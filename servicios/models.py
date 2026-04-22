from django.db import models
from ckeditor.fields import RichTextField

class Proyecto (models.Model):
    folio = models.CharField(max_length=12)
    proyecto = models.TextField() 
    empresa = models.TextField() 
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modificacion") 

# Cambiar el nombre del objeto
    def __str__(self):
        return self.proyecto

    class Meta:
       verbose_name = "Proyecto"
       verbose_name_plural ="Proyectos"
       ordering = ["-created"]
    

class Servicio(models.Model): 
    nombre = models.TextField()
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modificacion")

    def __str__(self):
        return self.nombre


class Resena(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    mensaje = RichTextField(null=True, blank=True)
    calificacion = models.IntegerField()  # 🔥 IMPORTANTE
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name = "Resena"
        verbose_name_plural = "Reseñas"
        ordering = ["-created"]

class Cotizacion(models.Model):

    ESTATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En proceso'),
        ('enviado', 'Enviado'),
        ('rechazado', 'Rechazado'),
    ]

    nombre = models.CharField(max_length=100)

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    descripcion = models.TextField()

    estatus = models.CharField(
        max_length=10,
        choices=ESTATUS_CHOICES,
        default='pendiente'
    )

    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # 🔥 sincroniza todas las respuestas sin provocar loop
        Respuesta.objects.filter(
            cotizacion=self
        ).exclude(
            estatus=self.estatus
        ).update(estatus=self.estatus)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"
        ordering = ["-created"]


class Respuesta(models.Model):

    cotizacion = models.ForeignKey(
        Cotizacion,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    mensaje = RichTextField(null=True, blank=True)

    estatus = models.CharField(
        max_length=10,
        choices=Cotizacion.ESTATUS_CHOICES,
        default='pendiente'
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        
        if self.cotizacion and self.cotizacion.estatus != self.estatus:
            Cotizacion.objects.filter(
                id=self.cotizacion.id
            ).update(estatus=self.estatus)

    def __str__(self):
        return f"Respuesta a {self.cotizacion} - {self.estatus}"

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"

class Descripcion(models.Model):
    servicio = models.ForeignKey(
    Servicio,
    on_delete=models.CASCADE,
    related_name="descripcion_servicio"
)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.servicio.nombre

    class Meta:
        verbose_name = "Descripcion"
        verbose_name_plural = "DescripcionServicios"
        ordering = ["-created"]