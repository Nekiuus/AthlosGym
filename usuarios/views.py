# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rol = 'cliente'
            usuario.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def inicio_privado(request):
    return render(request, 'index.html')



def inicio_publico(request):
    return render(request, 'inicio.html')

def logout_usuario(request):
    logout(request)
    return redirect('inicio')  # Redirige a la página pública
