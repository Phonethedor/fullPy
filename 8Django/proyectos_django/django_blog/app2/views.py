from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    context = {
        "name" : "Noelle",
        "favourite_color" : "turquoise",
        "pets" : ["Bruce", "Fitz", "Georgie"]
    }

    return render(request, "index.html", context)

class inicio(TemplateView):
    template_name = 'inicio.html'

class info(TemplateView):
    template_name = 'info.html'
    