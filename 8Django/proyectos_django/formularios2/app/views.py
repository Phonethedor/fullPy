from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def obtenerDatos(request):
    nombre = request.POST['nombre']
    rut = request.POST['rut']
    profesion= request.POST['profesion']
    sexo = request.POST['genero']
    edad = request.POST['edad']
    context = {
        "nombre_pagina": nombre,
        "rut_pagina": rut,
        "profesion_pagina": profesion,
        "sexo_pagina": sexo,
        "edad_pagina": edad
    }

    return render(request, "misdatos.html", context)