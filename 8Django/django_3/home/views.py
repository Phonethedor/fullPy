from .models import Prueba
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

class PruebaView(TemplateView):
    template_name = "prueba.html"

class PruebaListView(ListView):
    template_name = "lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0', '1', '2', '3', '5', '10', '20']

class ListarPrueba(ListView):
    template_name = "lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'

class CreateViewPrueba(CreateView):
    template_name = "agregar.html"
    model = Prueba
    fields = ['titulo','subtitulo','cantidad']