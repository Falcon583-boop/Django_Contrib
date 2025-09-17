from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def agregar_a_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito = request.session.get('carrito', [])
    carrito.append(libro.id)
    request.session['carrito'] = carrito
    messages.success(request, f'"{libro.titulo}" agregado al carrito de préstamos.')
    return redirect('lista_libros')
