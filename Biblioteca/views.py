# from django.shortcuts import render <-- esta libreria no
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer
# Create your views here.
class Modelo_1_ViewSet(viewsets.ModelViewSet):
# acá creamos una QUERY a nuestra tabla, trayendo
    queryset = programmer.objects.all()
# Agregamos la clase ProgrammerSerializer que ya
    serializer_class = ProgrammerSerializer
