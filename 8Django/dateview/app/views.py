from django.shortcuts import render, HttpResponse
from django.http import response
from time import gmtime, strftime, localtime

def date(request):
    context = {
        "time" : [
            strftime("%d " "%b " "%y", localtime()),
            strftime("%H: %M: %S", localtime())
            ]
    }

    return render(request, 'dateview.html', context)