from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse
from django.template import Template, Context

def root(request):
    return redirect("/blogs")


def index(request):
    return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')


def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')


def create(request):
    return redirect("/")


def show(request,numero):
    numero = numero

    documento = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Show</title>
            </head>
            <body>
                <h1 style="text-align: center;">placeholder para mostrar el blog numero %s</h1>
            </body>
        </html>
    """ %(numero)
    return HttpResponse(documento)


def edit(request,numero):
    numero = numero

    documento = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Show</title>
            </head>
            <body>
                <h1 style="text-align: center;">placeholder para editar el blog numero %s</h1>
            </body>
        </html>
    """ %(numero)
    return HttpResponse(documento)

def destroy(request):
    return redirect("/blogs")

def json(request):
    datos = {
        'meh': True
    }
    return JsonResponse(datos)

def datos(request):
    array = [1,2,3,4,5,6, 'op']

    template = open("C:/Users/alvar\Desktop/fullPy/8Django/proyectos_django/django_blog/blog/paginas/index.html")
    read = Template(template.read())
    template.close()
    contexto = Context({'Datos':array})
    documento = read.render(contexto)

    return HttpResponse(documento)