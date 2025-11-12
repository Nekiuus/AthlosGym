# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    rol = models.CharField(max_length=20, choices=[
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
        ('trabajador', 'Trabajador'),
    ])

    