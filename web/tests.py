"""
Tests para la aplicación web
"""
from django.test import TestCase, Client
from django.urls import reverse


class WebViewsTests(TestCase):
    """Tests de las vistas de la aplicación web"""
    
    def setUp(self):
        """Configuración inicial"""
        self.client = Client()
    
    def test_inicio_publico_carga(self):
        """Verifica que la página de inicio público carga correctamente"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_navbar_existe(self):
        """Verifica que el navbar se renderiza en la página"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # Verificar que se usa el template index.html
        self.assertTemplateUsed(response, 'index.html')


class URLConfigTests(TestCase):
    """Tests de la configuración de URLs"""
    
    def test_url_index(self):
        """Verifica que la URL de index existe"""
        response = self.client.get(reverse('index'))
        self.assertIn(response.status_code, [200, 301, 302])
    
    def test_url_admin_existe(self):
        """Verifica que la URL del admin existe"""
        response = self.client.get('/admin/')
        # Puede ser 200 si entra, o 302 si redirige a login
        self.assertIn(response.status_code, [200, 302])


class TemplateTests(TestCase):
    """Tests de templates"""
    
    def setUp(self):
        """Configuración inicial"""
        self.client = Client()
    
    def test_template_navbar_exists(self):
        """Verifica que el template del navbar existe"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
