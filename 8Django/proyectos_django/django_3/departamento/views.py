from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento

class ListarPrueba(ListView):
    template_name = "lista_prueba2.html"
    model = Departamento
    context_object_name = 'lista'