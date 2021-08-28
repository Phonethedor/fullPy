from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

datos = {
    'cuenta' : 1,
    'palabra' : get_random_string()
}

def index(request):
    return render(request, "index.html", datos)

def generar(request):
    datos['cuenta'] += 1
    datos['palabra'] = get_random_string(length=14)
    return redirect('/')

def limpiar(request):
    datos['cuenta'] = 1
    return redirect('/')