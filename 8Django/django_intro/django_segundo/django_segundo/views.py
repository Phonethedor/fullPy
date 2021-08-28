from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    return HttpResponse('Segundo proyecto y que PaZaH')

def chao(request):
    return HttpResponse('Erai po')

def ht(request):

    documento = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Response HTML</title>
            </head>
            <body>
                <h1 style="text-align: center;">CaChaH LoKo</h1>
            </body>
        </html>
    """ #brigioooooo

    return HttpResponse(documento)

def date(request):
    fechaHora = datetime.datetime.now()
    
    documento = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Date and Time</title>
            </head>
            <body>
                <h1 style="text-align: center;">Fecha y Hora actual: %s</h1>
            </body>
        </html>
    """ %fechaHora

    return HttpResponse(documento)

def parametros(request, year):
    edad = 2021 - year

    documento = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>nacimiento</title>
            </head>
            <body>
                <h1 style="text-align: center;">Su YEAR de nacimiento es: %s</h1>
                <h2 style="text-align: center;">Su edad es %s , verdad?</h2>
            </body>
        </html>
    """ %(year, edad)

    return HttpResponse(documento)

#importando paginas .html

def op(request):
    page = open("C:/Users/alvar/Desktop/fullPy/8Django/proyectos_django/django_intro/django_segundo/django_segundo./paginas/pagina.html")

    read = Template(page.read())
    page.close()

    context = Context()

    documento = read.render(context)

    return HttpResponse(documento)

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def op2(request):
    #nombre = 'Alvaro'
    #apellido = 'Castillo'
    per1 = Persona("Alvaro","Castillo")
    fechaHora = datetime.datetime.now()

    page = open("C:/Users/alvar/Desktop/fullPy/8Django/proyectos_django/django_intro/django_segundo/django_segundo./paginas/pagina1.html")

    read = Template(page.read())
    page.close()

    context = Context({"fecha_hora": fechaHora,"nombre_persona":per1.nombre, "apellido_persona": per1.apellido})

    documento = read.render(context)

    return HttpResponse(documento)


    
