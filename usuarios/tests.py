"""
Tests para la aplicación de usuarios
"""
from django.test import TestCase, Client
from django.urls import reverse
from .models import Usuario
from .forms import RegistroForm, LoginForm


class UsuarioModelTests(TestCase):
    """Prueba 1: Tests del modelo Usuario"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            telefono='1234567890',
            direccion='Calle Principal 123',
            rol='cliente'
        )
    
    def test_crear_usuario_cliente(self):
        """Verifica que se puede crear un usuario con rol cliente"""
        usuario = Usuario.objects.get(username='testuser')
        self.assertEqual(usuario.username, 'testuser')
        self.assertEqual(usuario.email, 'test@example.com')
        self.assertEqual(usuario.rol, 'cliente')
        self.assertEqual(usuario.telefono, '1234567890')
    
    def test_usuario_tiene_atributos_correctos(self):
        """Verifica que el usuario tiene todos los atributos esperados"""
        usuario = Usuario.objects.get(username='testuser')
        self.assertTrue(hasattr(usuario, 'telefono'))
        self.assertTrue(hasattr(usuario, 'direccion'))
        self.assertTrue(hasattr(usuario, 'rol'))
    
    def test_usuario_rol_valido(self):
        """Verifica que el rol del usuario es uno de los valores válidos"""
        usuario = Usuario.objects.get(username='testuser')
        roles_validos = ['cliente', 'admin', 'trabajador']
        self.assertIn(usuario.rol, roles_validos)
    
    def test_usuario_autenticacion(self):
        """Verifica que se puede autenticar el usuario"""
        usuario = Usuario.objects.get(username='testuser')
        self.assertTrue(usuario.check_password('testpass123'))
    
    def test_crear_usuario_admin(self):
        """Verifica que se puede crear un usuario administrador"""
        admin_user = Usuario.objects.create_user(
            username='admin_user',
            email='admin@example.com',
            password='adminpass123',
            rol='admin'
        )
        self.assertEqual(admin_user.rol, 'admin')


class RegistroFormTests(TestCase):
    """Prueba 2: Tests del formulario de registro"""
    
    def test_formulario_registro_valido(self):
        """Verifica que el formulario de registro acepta datos válidos"""
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'telefono': '9876543210',
            'direccion': 'Avenida Secundaria 456',
        }
        form = RegistroForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
    
    def test_formulario_registro_contrasenas_diferentes(self):
        """Verifica que el formulario rechaza contraseñas diferentes"""
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'DifferentPass123!',
        }
        form = RegistroForm(data=form_data)
        self.assertFalse(form.is_valid())
    
    def test_formulario_registro_usuario_duplicado(self):
        """Verifica que el formulario rechaza usuarios duplicados"""
        # Crear un usuario primero
        Usuario.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='testpass123'
        )
        
        # Intentar registrar con el mismo username
        form_data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }
        form = RegistroForm(data=form_data)
        self.assertFalse(form.is_valid())


class UsuarioViewsTests(TestCase):
    """Prueba 3: Tests de las vistas de usuarios"""
    
    def setUp(self):
        """Configuración inicial"""
        self.client = Client()
        self.usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            rol='cliente'
        )
    
    def test_pagina_registro_carga(self):
        """Verifica que la página de registro carga correctamente"""
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/registro.html')
    
    def test_registro_usuario_exitoso(self):
        """Verifica que el registro de usuario funciona"""
        response = self.client.post(reverse('registro'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
            'telefono': '1234567890',
            'direccion': 'Calle Test 789',
        })
        
        # Verificar que el usuario fue creado
        self.assertTrue(Usuario.objects.filter(username='newuser').exists())
    
    def test_login_usuario_exitoso(self):
        """Verifica que el login de usuario funciona"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        
        # Verificar que la sesión contiene el usuario
        self.assertIn('_auth_user_id', self.client.session)
    
    def test_login_usuario_invalido(self):
        """Verifica que login rechaza credenciales inválidas"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        
        # Verificar que no hay usuario en la sesión
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def test_logout_usuario(self):
        """Verifica que logout funciona correctamente"""
        # Primero loguearse
        self.client.login(username='testuser', password='testpass123')
        
        # Luego hacer logout
        response = self.client.get(reverse('logout'))
        
        # Verificar que la sesión está vacía
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def test_inicio_privado_sin_autenticacion(self):
        """Verifica que inicio privado redirige si no está autenticado"""
        response = self.client.get(reverse('inicio'), follow=False)
        # Debe redirigir a login
        self.assertEqual(response.status_code, 302)
    
    def test_inicio_privado_con_autenticacion(self):
        """Verifica que inicio privado se ve si está autenticado"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
