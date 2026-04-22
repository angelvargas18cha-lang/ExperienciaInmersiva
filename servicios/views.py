from django.shortcuts import render, redirect
from .models import Proyecto
from .models import Servicio
from .forms import ResenaForm 
from django.shortcuts import get_object_or_404
from .models import Respuesta
from .models import Cotizacion
from .models import Descripcion
from .models import Resena
import os

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})


def proyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'servicios/proyectosrealizados.html', {'proyectos': proyectos})

def cotizacion(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    comentarios = Resena.objects.filter(servicio=servicio)
    descripciones = Descripcion.objects.filter(servicio=servicio)

    if request.method == 'POST':
        
        # RESEÑA
        if 'mensaje' in request.POST:
            Resena.objects.create(
                servicio=servicio,
                usuario=request.POST.get('usuario'),
                mensaje=request.POST.get('mensaje'),
                calificacion=request.POST.get('calificacion') or 0
            )
            return redirect('cotizacion', id=servicio.id)

        #  COTIZACIÓN
        else:
            Cotizacion.objects.create(
                servicio=servicio,
                nombre=request.POST.get('nombre'),
                correo=request.POST.get('correo'),
                telefono=request.POST.get('telefono'),
                descripcion=request.POST.get('descripcion')
            )
            return redirect('cotizacion', id=servicio.id)

    return render(request, "servicios/cotizacion.html", {
        'servicio': servicio,
        'comentarios': comentarios,
        'descripciones': descripciones
    })



def registrar(request):
    return render(request, 'servicios/cotizacion.html')    


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        telefono = request.POST.get("telefono")
        descripcion = request.POST.get("descripcion")

        Cotizacion.objects.create(
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            descripcion=descripcion,
            servicio=None  
        )

        return redirect('Contacto') 

    return render(request, "servicios/contacto.html")


def video1(request):
    return render(request, 'servicios/video1.html') 

def video2(request):
    return render(request, 'servicios/video2.html') 

    
