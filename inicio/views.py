from django.shortcuts import render


def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def servicios(request):
    return render(request,"inicio/servicios.html")

def proyectosrealizados(request):
    return render(request,"inicio/proyectosrealizados.html")

def blog(request):
    return render(request,"inicio/blog.html")

def contacto(request):
    return render(request, 'servicios/contacto.html') 