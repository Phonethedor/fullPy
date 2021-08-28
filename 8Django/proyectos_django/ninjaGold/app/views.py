from django.shortcuts import render, redirect
from random import randint
from datetime import datetime

def index(request):
    if 'gold_amount' not in request.session:
        request.session['gold_amount'] = 0
        request.session['plays'] = []
    
    return render(request, 'index.html')



def process_money(request):
    
    time = datetime.now().strftime("$%Y-%m-%d %H:%M:%S %p")

    if "farm" in request.POST:
        gold = randint(10, 20)
        request.session['gold_amount'] += gold
        request.session['plays'].append([gold, 'farm', time])
    elif "house" in request.POST:
        gold = randint(5,10)
        request.session['gold_amount'] += gold
        request.session['plays'].append([gold, 'house', time])
    elif "cave" in request.POST:
        gold = randint(2,5)
        request.session['gold_amount'] += gold
        request.session['plays'].append([gold, 'cave', time])
    elif "casino" in request.POST:
        gold = randint(-50,50)
        request.session['gold_amount'] += gold
        request.session['plays'].append([gold, 'casino', time])

    return redirect('/')