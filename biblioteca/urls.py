from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('agregar/<int:libro_id>/', views.agregar_a_carrito, name='agregar_a_carrito'),
]
