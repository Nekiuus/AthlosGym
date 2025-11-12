from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def producto(request):
    return render(request, 'producto.html')

def carritocompras(request):
    return render(request, 'carritocompras.html')

@login_required
def inicio_privado(request):
    return render(request, 'web/index.html')

