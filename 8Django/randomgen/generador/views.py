from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "contador" not in request.session.keys():
        print ("primera visita")
        request.session['contador'] = 0
    else:
        request.session['contador'] += 1
    context = {
        "contador": request.session['contador'],
        "genAzar": get_random_string(length=14)
    }
    return render(request, "index.html", context)

def reinicio(request):
    request.session['contador'] = 0
    return redirect('/')