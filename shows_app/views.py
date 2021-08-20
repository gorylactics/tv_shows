from django.shortcuts import render , redirect
from .models import Show


def base(request):
    return redirect('/shows')


def index(request):
    print(request.POST)
    contexto = {
        'titulo' : 'All Shows',
        'programas' :  Show.objects.all()
    }
    if request.method == 'POST':
        return redirect('/')
    if request.method == 'GET':
        return render(request, 'shows_app/index.html' , contexto)

def new(request):
    contexto = {
        'titulo' : 'New Program'
    }
    return render(request, 'shows_app/new.html', contexto)
