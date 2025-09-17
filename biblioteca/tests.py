from django.test import TestCase
from django.urls import reverse
from .models import Autor, Libro

class BibliotecaModelTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nombre='Gabriel García Márquez', nacionalidad='Colombia')
        self.libro = Libro.objects.create(titulo='Cien Años de Soledad', autor=self.autor, disponible=True)

    def test_str_autor(self):
        self.assertEqual(str(self.autor), 'Gabriel García Márquez')

    def test_str_libro(self):
        self.assertEqual(str(self.libro), 'Cien Años de Soledad')

class BibliotecaViewsTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nombre='Jorge Luis Borges')
        self.libro = Libro.objects.create(titulo='Ficciones', autor=self.autor, disponible=True)

    def test_lista_libros_status(self):
        response = self.client.get(reverse('lista_libros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ficciones')

    def test_agregar_a_carrito_session_and_message(self):
        response = self.client.get(reverse('agregar_a_carrito', args=[self.libro.id]), follow=True)
        # Verificar que redirige OK
        self.assertEqual(response.status_code, 200)
        # Verificar que el libro quedó en la sesión
        session_carrito = self.client.session.get('carrito', [])
        self.assertIn(self.libro.id, session_carrito)
        # Verificar mensaje
        messages = list(response.context['messages'])
        self.assertTrue(any('agregado al carrito' in str(m) for m in messages))
