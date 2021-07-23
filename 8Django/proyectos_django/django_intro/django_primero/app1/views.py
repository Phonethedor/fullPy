from django.http.response import HttpResponse
from django.shortcuts import render

def paginaInicio(request):
    return HttpResponse("Hola mundo!")