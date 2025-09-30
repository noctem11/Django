from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Nacionalidad_Serializer, Autor_Serializer, Comuna_Serializer, Direccion_Serializer, Biblioteca_Serializer, Lector_Serializer, Libro_Serializer, Genero_Serializer, Prestamo_Serializer
from .models import Nacionalidad, Autor, Comuna, Direccion, Biblioteca, Lector, Genero, Libro, Prestamo


def pagina_inicio(request): 
    return render (request, 'mi_app/inicio.html')

class Nacionalidad_ViewSet(viewsets.ModelViewSet):

    queryset = Nacionalidad.objects.all()
    serializer_class = Nacionalidad_Serializer

class Autor_ViewSet(viewsets.ModelViewSet):

    queryset = Autor.objects.all()
    serializer_class = Autor_Serializer

class Comuna_ViewSet(viewsets.ModelViewSet):

    queryset = Comuna.objects.all()
    serializer_class = Comuna_Serializer

class Direccion_ViewSet(viewsets.ModelViewSet):

    queryset = Direccion.objects.all()
    serializer_class = Direccion_Serializer

class Biblioteca_ViewSet(viewsets.ModelViewSet):

    queryset = Biblioteca.objects.all()
    serializer_class = Biblioteca_Serializer

class Lector_ViewSet(viewsets.ModelViewSet):

    queryset = Lector.objects.all()
    serializer_class = Lector_Serializer

class Libro_ViewSet(viewsets.ModelViewSet):

    queryset = Libro.objects.all()
    serializer_class = Libro_Serializer

class Genero_ViewSet(viewsets.ModelViewSet):

    queryset = Genero.objects.all()
    serializer_class = Genero_Serializer

class Prestamo_ViewSet(viewsets.ModelViewSet):

    queryset = Prestamo.objects.all()
    serializer_class = Prestamo_Serializer

