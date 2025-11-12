from django.urls import path
from .views import registro_usuario, login_usuario
from .views import inicio_privado, inicio_publico, logout_usuario

urlpatterns = [
    path('', inicio_publico, name='main'),
    path('registro/', registro_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('inicio/', inicio_privado, name='inicio'),    
]
