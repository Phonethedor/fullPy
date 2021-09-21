from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.


def index(request):
    return redirect('/shows')


def show(request):
    context = {
        'lista_shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)


def addShow(request):
    return render(request, 'addshow.html')


def showAdd(request):
    show = Show.objects.create(
            title=request.POST['title'], 
            network=request.POST['network'], 
            release_date=request.POST['release'], 
            description=request.POST['description']
    )
    return redirect(f'/shows/{show.id}')


def TvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'TVShow.html', context)


def EditShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'EditShow.html', context)


def UpdateShow(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{id}')


def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')